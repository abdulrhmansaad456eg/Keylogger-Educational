# Educational Keylogger Demo 

**For educational purposes only. Use with explicit user consent.**

This project demonstrates advanced Python concepts:
- Event-driven input monitoring (`pynput`)
- Multi-threading
- Real-time clipboard monitoring
- Mandatory GUI consent dialog (Tkinter)
- Silent background execution
- Easy conversion to standalone `.exe`

###  Features
- Logs keystrokes, mouse clicks, and clipboard changes
- Saves dated logs in `~/EducationalKeylogger`
- Shows a clear consent dialog **every single time** it runs
- Fully educational & ethical design

###  Important Legal Notice
This tool can **only** be used on devices where **every user has given explicit, informed consent**.  
Any unauthorized use is illegal in most countries.  
I do **not** support or endorse malicious applications.

### How to Use
1. `pip install -r requirements.txt`
2. `python keylogger.py`
3. Accept the consent dialog
4. Logs are saved automatically

### Build .exe (Windows)
```bash
pyinstaller --onefile --noconsole keylogger.py
