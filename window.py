import tkinter as tk
from scraper import Scraper
from local import Local

class DriverUpdateChecker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Driver Update Checker")
        self.root.geometry("400x200")

        self.setup_ui()

    def setup_ui(self):
        label = tk.Label(self.root, text="Check for Graphics Driver Updates", font=("Arial", 14))
        label.pack(pady=10)

        check_button = tk.Button(self.root, text="Check Update", command=self.check_update)
        check_button.pack(pady=10)

        self.current_version_label = tk.Label(self.root, text="Current Version: Not Checked", font=("Arial", 12))
        self.current_version_label.pack(pady=5)

        self.latest_version_label = tk.Label(self.root, text="Latest Version: Not Checked", font=("Arial", 12))
        self.latest_version_label.pack(pady=5)

    def check_update(self):
        current_version = Local.get_graphics_driver_version()
        latest_version = Scraper.fetch_latest_version()

        self.current_version_label.config(text=f"Current Version: {current_version[:3]}.{current_version[3:]}")
        
        if latest_version.startswith("Error"):
            self.latest_version_label.config(text=f"Latest Version: {latest_version}")
        else:
            latest_version_number = latest_version.split()[2]  # Assuming format "NVIDIA GeForce 560.70 WHQL"
            
            if current_version !=  latest_version_number.replace('.', ''):
                self.latest_version_label.config(text=f"Latest Version: {latest_version_number} (Update Available)")
            else:
                self.latest_version_label.config(text=f"Latest Version: {latest_version_number} (Up to Date)")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = DriverUpdateChecker()
    app.run()
