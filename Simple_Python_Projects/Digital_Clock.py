from tkinter import *
import time

def main():
  root = Tk()
  root.title("Digital Clock with Date")

  # Create the time label. winks!
  time_label = Label(root, font=("TimesNewRoman", 76, "bold italic"))
  time_label.pack()

  # Update the time every second, for the 12hr(AM/PM) clock
  def update_time():
    am_or_pm = time.strftime("%p")
    current_time = time.strftime("%I:%M:%S" + " " + am_or_pm)
    current_date = time.strftime("%A, %B %d, %Y")

    time_label.config(text=current_time + "\n" + current_date)
    time_label.after(1000, update_time)

  update_time()
  root.mainloop()

if __name__ == "__main__":
  main()
