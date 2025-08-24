import tkinter as tk
from tkinter import ttk


class BreakScreen(tk.Toplevel):
    def __init__(self, on_end=None):
        super().__init__()
        self.duration = 20
        self.on_end = on_end

        self.attributes("-fullscreen", True)
        self.attributes("-topmost", True)
        self.config(bg="black")
        self.config(cursor="none")

        self.label = tk.Label(
            self,
            text=self.duration,
            bg="black",
            fg="white",
            font=("Arial", 100),
        )

        self.label.pack(expand=True)

        self.countdown()

    def countdown(self):
        if self.duration > 0:
            self.label["text"] = self.duration
            self.duration -= 1
            self.after(1000, self.countdown)

        else:
            self.close_break()

    def close_break(self):
        self.on_end()
        self.destroy()


class EyeCareApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("20_20_20 Eye Care Timer")

        self.app_width = 600
        self.app_height = 400
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.geometry(
            f"{self.app_width}x{self.app_height}+{int(((self.screen_width)/2) - self.app_width/2)}+{int(((self.screen_height)/2) - self.app_height/2)}"
        )

        self.config(bg="#333")
        self.resizable(False, False)



        self.protocol('WM_DELETE_WINDOW', self.withdraw)

        self.timer = ttk.Label(
            master=self,
            text="00",
            font=("cascadia mono", 100),
            background="#333",
            foreground="#fff",
        )

        self.timer.pack(expand=True)

        self.action_frame = tk.Frame(self)
        self.action_frame.pack(fill="x")

        self.exit_btn = tk.Button(
            self.action_frame,
            text="Exit",
            font=("cascadia mono", 16),
            relief="flat",
            bg="darkred",
            fg="#fff",
            cursor="hand2",
            command=self.destroy,
        )

        self.reset_btn = tk.Button(
            self.action_frame,
            text="Reset Time",
            font=("cascadia mono", 16),
            relief="flat",
            bg="dodgerblue",
            fg="#fff",
            cursor="hand2",
            command=self.reset_time,
        )

        self.pause_btn = tk.Button(
            self.action_frame,
            text="Pause",
            font=("cascadia mono", 16),
            relief="flat",
            bg="Orange",
            fg="#fff",
            cursor="hand2",
            command=self.pause,
        )

        self.exit_btn.pack(fill="x", side="left", expand=True)
        self.reset_btn.pack(fill="x", side="left", expand=True)
        self.pause_btn.pack(fill="x", side="left", expand=True)

        self.time = 60 * 20  # 20 minutes in second
        self.paused = False
        self.running = False

        self.countdown()

        self.mainloop()

    def countdown(self):
        if not self.paused:
            self.running = True
            minutes, seconds = divmod(self.time, 60)

            self.timer["text"] = f"{int(minutes):02d}:{int(seconds):02d}"

            if self.time > 0:
                self.time -= 1
                self.after(1000, self.countdown)

            else:
                self.running = False
                self.break_screen()

        else:
            self.after(1000, self.countdown)

    def break_screen(self):
        self.paused = True

        def on_end_function():
            self.paused = False
            self.time = 20 * 60
            self.countdown()

        break_screen = BreakScreen(on_end=on_end_function)
        break_screen.grab_set()

    def pause(self):
        self.paused = not self.paused

        self.pause_btn.config(text="Resume" if self.paused else "Pause")
        
        if not self.paused and not self.running:
            self.countdown()

    def reset_time(self):
        self.time = 20 * 60


EyeCareApp()
