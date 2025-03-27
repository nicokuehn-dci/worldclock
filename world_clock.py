import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

class WorldClock(tk.Tk):
    """A simple World Clock application using Tkinter."""
    def __init__(self):
        super().__init__()
        self.title("World Clock")
        self.geometry("400x250")
        self.configure(bg='#2E3440')

        # Time display label
        self.time_label = tk.Label(
            self,
            font=("Arial", 48),
            fg="#88C0D0",
            bg="#2E3440"
        )
        self.time_label.pack(expand=True)

        # Timezone name label
        self.timezone_name_label = tk.Label(
            self,
            font=("Arial", 14),
            fg="#88C0D0",
            bg="#2E3440"
        )
        self.timezone_name_label.pack()

        # Dropdown for selecting timezones
        self.timezone_var = tk.StringVar()
        self.timezones = sorted(pytz.all_timezones)

        self.combobox = ttk.Combobox(
            self,
            textvariable=self.timezone_var,
            values=self.timezones,
            font=("Arial", 12),
            state="readonly"
        )
        self.combobox.set("UTC")  # Set default timezone
        self.combobox.pack(pady=10)
        self.combobox.bind("<<ComboboxSelected>>", self.update_time)

        # Start updating the time
        self.update_time()

    def update_time(self, event=None):
        """Update the displayed time based on the selected timezone."""
        selected_timezone = self.timezone_var.get()
        if not selected_timezone:
            selected_timezone = "UTC"  # Default to UTC if no timezone is selected
        tz = pytz.timezone(selected_timezone)
        current_time = datetime.now(tz).strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.timezone_name_label.config(text=selected_timezone)
        self.after(1000, self.update_time)  # Update every second

if __name__ == "__main__":
    app = WorldClock()
    app.mainloop()
