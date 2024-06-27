import tkinter as tk
from scraper import Scraper as sc
from local import Local as lc

def main_window():
    global current_version_label
    global latest_version_label
    
    root = tk.Tk()
    root.title("Driver Update Checker")
    root.geometry("400x200")

    label = tk.Label(root, text="Check for Graphics Driver Updates", font=("Arial", 14))
    label.pack(pady=10)

    check_button = tk.Button(root, text="Check Update", command=check_update)
    check_button.pack(pady=10)

    current_version_label = tk.Label(root, text="Current Version: Not Checked", font=("Arial", 12))
    current_version_label.pack(pady=5)

    latest_version_label = tk.Label(root, text="Latest Version: Not Checked", font=("Arial", 12))
    latest_version_label.pack(pady=5)

    root.mainloop()

def check_update():
    current_version = lc.get_graphics_driver_version()
    latest_version = sc.fetch_latest_version()
    
    current_version_label.config(text=f"Current Version: {current_version}")
    latest_version_label.config(text=f"Latest Version: {latest_version}")
    
    if current_version.split(" - ")[-1] != latest_version.split(" - ")[-1]:
        latest_version_label.config(text=f"Latest Version: {latest_version} (Update Available)")
    else:
        latest_version_label.config(text=f"Latest Version: {latest_version} (Up to Date)")

if __name__ == "__main__":
    main_window()