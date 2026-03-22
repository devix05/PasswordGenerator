import tkinter as tk
import tkinter.font as tkFont
import string
import random

fenster = tk.Tk()
fenster.title("Passwortgenerator")
fenster.geometry("420x260")
fenster.configure(bg="#1e1e1e")

default_font = tkFont.Font(family="Segoe UI", size=12)
fenster.option_add("*Font", default_font)
fenster.option_add("*Foreground", "#ffffff")
fenster.option_add("*Background", "#1e1e1e")

title_font = tkFont.Font(family="Segoe UI", size=20, weight="bold")
tk.Label(fenster, text="🔐 Passwortgenerator", font=title_font, bg="#1e1e1e").pack(pady=(15, 10))

frame = tk.Frame(fenster, bg="#1e1e1e")
frame.pack(pady=5)

tk.Label(frame, text="Länge wählen:", bg="#1e1e1e").pack(side="left", padx=5)

input_var = tk.IntVar(value=12)
spin = tk.Spinbox(frame, from_=4, to=40, textvariable=input_var, width=5, bg="#2d2d2d", fg="white", insertbackground="white", highlightbackground="#3c3c3c", relief="flat")
spin.pack(side="left")

out = tk.Entry(fenster, width=35, bg="#2d2d2d", fg="white", insertbackground="white", relief="flat")
out.pack(pady=10, ipady=4)

def gen():
    n = int(input_var.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = "".join(random.choice(chars) for _ in range(n))

    out.delete(0, "end")
    out.insert(0, pwd)

def copyToClip():
    fenster.clipboard_clear()
    fenster.clipboard_append(out.get())

btn_style = {
    "bg": "#0078D4",
    "activebackground": "#005A9E",
    "fg": "white",
    "activeforeground": "white",
    "relief": "flat",
    "width": 15,
    "height": 1
}

button_frame = tk.Frame(fenster, bg="#1e1e1e")
button_frame.pack(pady=5)

tk.Button(button_frame, text="🔄 Generieren", command=gen, **btn_style).pack(side="left", padx=5)
tk.Button(button_frame, text="📋 Kopieren", command=copyToClip, **btn_style).pack(side="left", padx=5)

fenster.mainloop()
