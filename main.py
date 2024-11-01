import tkinter as tk
from tkinter import messagebox
from pynput import keyboard
import threading
import time

# Global flags and status
status = True
last_key_press_time = time.time()

def on_press(key):
    global last_key_press_time
    last_key_press_time = time.time()  # Update the time when any key is pressed

def death_timer():
    global status, last_key_press_time
    while status:
        time.sleep(0.1)  # Small delay to avoid excessive CPU usage
        if time.time() - last_key_press_time > 5:  # If more than 5 seconds pass since the last key press
            status = False
            messagebox.showinfo("Time limit reached", "You took too long to type!")
            para_text.delete('1.0', tk.END)
            para_text.config(state=tk.DISABLED)
            break

def start_timer():
    para_text.config(state=tk.NORMAL)
    global status, last_key_press_time
    status = True
    last_key_press_time = time.time()
    threading.Thread(target=death_timer, daemon=True).start()

def start_typing_listener():

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


threading.Thread(target=start_typing_listener, daemon=True).start()


root = tk.Tk()
root.title("Dangerous Typing-Speed Test")

para = tk.LabelFrame(root, text="Paragraph", pady=10, padx=10)
para_text = tk.Text(para, height=10, width=70, state=tk.DISABLED, font=("Arial", 19), wrap=tk.WORD)
para_text.grid(row=0, column=0)
para.grid(row=0, column=0)

start_frame = tk.LabelFrame(root, text="Death Timer", padx=10, pady=10)
start_button = tk.Button(start_frame, text="Start", command=start_timer)
start_button.grid(row=0, column=0)
start_frame.grid(row=1, column=0)

root.mainloop()
