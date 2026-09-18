import sys
import os
import random
import customtkinter as ctk

def resource_path(dateiname):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, dateiname)
    return dateiname

def generiere_passwort(laenge, zeichen_menge):
    passwort = ""
    for i in range(laenge):
        zufallszeichen = random.choice(zeichen_menge)
        passwort = passwort + zufallszeichen
    return passwort


def button_geklickt():
    zeichen = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    if sonderzeichen_var.get():
        zeichen = zeichen + "!@#$%^&*"
    try:
        laenge = int(laenge_eingabe.get())
        anzahl = int(anzahl_eingabe.get())
    except ValueError:
        return

    textbox.delete("1.0", "end")
    for i in range(anzahl):
        neues_passwort = generiere_passwort(laenge, zeichen)
        textbox.insert("end", neues_passwort + "\n")

def speichere_passwoerter():
    inhalt = textbox.get("1.0", "end")
    with open("passwoerter.txt", "w") as f:
        f.write(inhalt)

def kopiere_passwort():
    try:
        markierter_text = textbox.get("sel.first", "sel.last")
        fenster.clipboard_clear()
        fenster.clipboard_append(markierter_text)
    except:
        pass

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")
fenster = ctk.CTk()
fenster.geometry("500x400")
fenster.title("Passwort Generator")
fenster.iconbitmap(resource_path("logo.ico"))

sonderzeichen_var = ctk.BooleanVar(value=False)
sonderzeichen_checkbox = ctk.CTkCheckBox(fenster, text="Mit Sonderzeichen", variable=sonderzeichen_var)
sonderzeichen_checkbox.pack(pady=5)

frame1 = ctk.CTkFrame(fenster)
frame1.pack(pady=5)
label1 = ctk.CTkLabel(frame1, text="Gewünschte Länge:")
label1.pack(side="left", padx=5)
laenge_eingabe = ctk.CTkEntry(frame1)
laenge_eingabe.pack(side="left", padx=5)

frame2 = ctk.CTkFrame(fenster)
frame2.pack(pady=5)
label2 = ctk.CTkLabel(frame2, text="Wie viele Passwörter?")
label2.pack(side="left", padx=5)
anzahl_eingabe = ctk.CTkEntry(frame2)
anzahl_eingabe.pack(side="left", padx=5)

kopieren_button = ctk.CTkButton(fenster, text="Markieres kopieren", command=kopiere_passwort)
kopieren_button.pack(pady=5)

button = ctk.CTkButton(fenster, text="Generieren", command=button_geklickt)
button.pack(pady=10)

speichern_button = ctk.CTkButton(fenster, text="Speichern", command=speichere_passwoerter)
speichern_button.pack(pady=5)

textbox = ctk.CTkTextbox(fenster, width=300, height=200)
textbox.pack(pady=10)

fenster.mainloop()
