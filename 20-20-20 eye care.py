"""
Created at ግንቦት 18 2016 ዓ.ም
"""

from tkinter import Tk, Button, Frame
from tkinter import ttk
import subprocess as sbp
from time import sleep
import platform as ptf


class App(Tk):
    def __init__(self):
        super().__init__()
        self.app_width = 600
        self.app_height = 400
        self.title("20-20-20 Eye Care Timer")
        self.geometry(
            f"{self.app_width}x{self.app_height}+{int(self.winfo_screenwidth()/2) - int(self.app_width/2)}+{int(self.winfo_screenheight()/2) - int(self.app_height/2)}"
        )
        self.resizable(False, False)
        self.config(bg="#333")

        self.protocol("WM_DELETE_WINDOW", self.background_running)

        self.time = 20 * 60
        self.running = False

        self.timer = ttk.Label(
            font=("cascadia mono", 100), background="#333", foreground="#fff"
        )

        self.action_frame = Frame(self)

        self.stop_working = Button(
            self.action_frame,
            relief="flat",
            text="Block Application",
            font=("cascadia mono", 16),
            bg="darkred",
            fg="#fff",
            cursor="hand2",
            command=lambda: self.destroy(),
        )

        self.reset_button = Button(
            self.action_frame,
            relief="flat",
            text="Reset Time",
            font=("cascadia mono", 16),
            bg="dodgerblue",
            fg="#fff",
            cursor="hand2",
            command=self.reset,
        )

        self.timer.pack(expand=True)
        self.action_frame.pack(fill="x")
        self.stop_working.pack(fill="x", side="left", expand=True)
        self.reset_button.pack(fill="x", side="left", expand=True)

        self.countdown()
        
        

        self.mainloop()

    def countdown(self):
        self.running = True
        min, sec = divmod(self.time, 60)

        self.timer["text"] = f"{int(min):02d}:{int(sec):02d}"

        if self.time > 0:
            self.time -= 1
            self.after(1000, self.countdown)
        else:
            self.running = False
            self.show_notification()
            sleep(20)
            self.time = 20 * 60
            self.countdown()

    def show_notification(self):
        platform = ptf.system()
        message = f'Time for a 20-20-20 break! Look at an object 20 feet away for 20 seconds to give your eyes a rest.'

        if platform == 'Windows':
        	sbp.run([f'powershell.exe -Command "msg * {message}"'],shell=True)
        elif platform == 'Linux':
            sbp.run([f'zenity --info --text="{message}"'],shell=True)
        elif platform == 'Darwin':
            sbp.run([f'osascript -e \'display dialog "{message}"\''],shell=True)

    
    def background_running(self):
        self.withdraw()

    def reset(self):
        self.time = 20 * 60


App()
