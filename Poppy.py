import tkinter as tk
from tkinter import ttk
from scraper import Scraper
from local import Local
import webbrowser

class DriverUpdateChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.after(201, lambda :self.root.iconbitmap('icon.ico'))
        self.root.title("Driver Update Checker")
        self.root.geometry("400x250")
        self.root.configure(bg='#1e1e1e')  # Dark background
        self.root.attributes('-alpha', 0.9)  # Translucent effect

        self.setup_ui()
        self.latest_version_number = None

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure button style
        style.configure('TButton', 
                        background='#333333', 
                        foreground='white', 
                        borderwidth=0, 
                        focusthickness=3, 
                        focuscolor='none')
        style.map('TButton', background=[('active', '#444444')])
        
        # Configure label style
        style.configure('TLabel', 
                        background='#1e1e1e', 
                        foreground='white')

        label = ttk.Label(self.root, text="Check for Graphics Driver Updates", font=("Arial", 14))
        label.pack(pady=10)

        check_button = ttk.Button(self.root, text="Check Update", command=self.check_update, style='TButton')
        check_button.pack(pady=10)

        self.current_version_label = ttk.Label(self.root, text="Current Version: Not Checked", font=("Arial", 12))
        self.current_version_label.pack(pady=5)

        self.latest_version_label = ttk.Label(self.root, text="Latest Version: Not Checked", font=("Arial", 12))
        self.latest_version_label.pack(pady=5)

        self.download_button = ttk.Button(self.root, text="Download Latest Driver", command=self.download_driver, style='TButton')
        self.download_button.pack(pady=10)
        self.download_button.pack_forget()

    def check_update(self):
        current_version = Local.get_graphics_driver_version()
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