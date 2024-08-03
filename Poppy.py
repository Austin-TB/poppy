import tkinter as tk
from scraper import Scraper
from local import Local
import webbrowser

class DriverUpdateChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.after(201, lambda :self.root.iconbitmap('icon.ico'))
        self.root.title("Driver Update Checker")
        self.root.geometry("400x250")

        self.setup_ui()
        self.latest_version_number = None

    def setup_ui(self):
        label = tk.Label(self.root, text="Check for Graphics Driver Updates", font=("Arial", 14))
        label.pack(pady=10)

        check_button = tk.Button(self.root, text="Check Update", command=self.check_update)
        check_button.pack(pady=10)

        self.current_version_label = tk.Label(self.root, text="Current Version: Not Checked", font=("Arial", 12))
        self.current_version_label.pack(pady=5)

        self.latest_version_label = tk.Label(self.root, text="Latest Version: Not Checked", font=("Arial", 12))
        self.latest_version_label.pack(pady=5)

        self.download_button = tk.Button(self.root, text="Download Latest Driver", command=self.download_driver)
        self.download_button.pack(pady=10)
        self.download_button.pack_forget()

    def check_update(self):
        current_version = Local.get_graphics_driver_version()
        # current_version = "47111"
        latest_version = Scraper.fetch_latest_version()

        self.current_version_label.config(text=f"Current Version: {current_version[:3]}.{current_version[3:]}")
        
        if latest_version.startswith("Error"):
            self.latest_version_label.config(text=f"Latest Version: {latest_version}")
            self.download_button.pack_forget()
        else:
            self.latest_version_number = latest_version.split()[2]
            
            if current_version != self.latest_version_number.replace('.', ''):
                self.latest_version_label.config(text=f"Latest Version: {self.latest_version_number} (Update Available)")
                self.download_button.pack()
            else:
                self.latest_version_label.config(text=f"Latest Version: {self.latest_version_number} (Up to Date)")
                self.download_button.pack_forget()
    def download_driver(self):
        if self.latest_version_number:
            url = f"https://in.download.nvidia.com/Windows/{self.latest_version_number}/{self.latest_version_number}-notebook-win10-win11-64bit-international-dch-whql.exe"
            webbrowser.open(url)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = DriverUpdateChecker()
    app.run()
