#https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203 for alarm sound download
import tkinter
from tkinter import messagebox
import tkinter as tk
import time
import os
from playsound import playsound

class AlarmClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alarm Clock")
        self.root.geometry("500x200")

        # Create the time entry fields and labels.
        global hourMin_entry1
        global message_entry2
        self.hourMin_entry1 = tk.Entry(self.root, width=15)
        self.hourMin_entry1.grid(row=0, column=3, padx=5, pady=5)
        self.message_entry2 = tk.Entry(self.root, width=30)
        self.message_entry2.grid(row=1, column=3, padx=5, pady=5)

        # Add labels for the time entry fields.
        hourMin_label1 = tk.Label(self.root, text="Enter time in 24hr format; hh:mm: ")
        hourMin_label1.grid(row=0, column=2, padx=5, pady=5)
        message_label2 = tk.Label(self.root, text="    Enter the message of the alarm: ")
        message_label2.grid(row=1, column=2, padx=5, pady=5)

        # Create a button to submit the alarm details.
        submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        submit_button.grid(row=2, column=3, padx=5, pady=5)

        # Create a label to display the alarm status.
        global Alarm_label3
        Alarm_label3 = tk.Label(self.root, text="")
        Alarm_label3.grid(row=3, column=3, padx=5, pady=5)
        self.root.mainloop()

    def play_alarm(self):
        playsound("Alarm-Slow-A3.mp3")
        Alarm_label3.config(text="Alarm Sound Playing>>>>")
        alarm_message = self.message_entry2.get()
        messagebox.showinfo("Alarm Message", f"The Alarm message is: {alarm_message}")

    def submit(self):
        global hourMin_entry1, message_entry2, Alarm_label3
        alarm_time = self.hourMin_entry1.get()
        self.pop_up_message(alarm_time)

        current_time = time.strftime("%H:%M")

        while alarm_time != current_time:
            current_time = time.strftime("%H:%M")
            time.sleep(1)

        if alarm_time == current_time:
            self.play_alarm()

    def pop_up_message(self, alarm_time):
        Alarm_label3.config(text="The Alarm is ON....")
        messagebox.showinfo("Alarm Clock", f"The Alarm is set to ring at: {alarm_time}")

if __name__ == "__main__":
    AlarmClock()
