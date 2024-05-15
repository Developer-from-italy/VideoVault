# Description: GUI for the VideoVault application
from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage
from pytube import YouTube
import ssl

# Fix SSL certificate issue
ssl._create_default_https_context = ssl._create_unverified_context

# Define paths
OUTPUT_PATH = Path(__file__).parent  # Percorso della cartella corrente
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/carlograncini/Developer/VideoVault/build/assets/frame0")  # Percorso degli asset grafici

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)  # Funzione per ottenere il percorso assoluto degli asset

# Initialize window
window = tk.Tk()  # Creazione della finestra principale
window.geometry("800x500")  # Dimensioni della finestra
window.configure(bg = "#2B2D42")  # Colore di sfondo della finestra

# Create canvas
canvas = Canvas(
    window,
    bg = "#2B2D42",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)  # Creazione di un canvas per disegnare elementi grafici
canvas.place(x = 0, y = 0)  # Posizionamento del canvas
canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    79.0,
    fill="#EDF2F4",
    outline=""
)  # Creazione di un rettangolo come intestazione
canvas.create_text(
    283.0,
    20.0,
    anchor="nw",
    text="VideoVault",
    fill="#000000",
    font=("MesloLGS NF Regular", 35 * -1)
)  # Testo del titolo "VideoVault"

# Entry field for YouTube link
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))  # Immagine di sfondo del campo di inserimento
entry_bg_1 = canvas.create_image(400.0, 156.0, image=entry_image_1)  # Posizionamento dell'immagine di sfondo
entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)  # Creazione del campo di inserimento del link
entry_1.place(x=125.0, y=136.0, width=550.0, height=38.0)  # Posizionamento del campo di inserimento

# Labels
title = tk.Label(window, text="Insert the link of the video", bg="#2B2D42", fg="white")  # Etichetta per l'inserimento del link
title.place(x=125.0, y=180.0)  # Posizionamento dell'etichetta
finishlabel = tk.Label(window, text="", bg="#2B2D42", fg="white")  # Etichetta per mostrare lo stato del download
finishlabel.place(x=125.0, y=220.0)  # Posizionamento dell'etichetta

# Functions for downloading
def startDownload():
    try:
        ytLink = entry_1.get()  # Ottiene il link inserito
        ytObject = YouTube(ytLink)  # Crea un oggetto YouTube
        video = ytObject.streams.get_highest_resolution()  # Ottiene il video alla risoluzione più alta
        title.config(text=ytObject.title)  # Aggiorna il titolo con il titolo del video
        finishlabel.config(text="")  # Reset dell'etichetta di stato
        video.download()  # Scarica il video
        finishlabel.config(text="Download finished")  # Aggiorna l'etichetta di stato
    except:
        finishlabel.config(text="The link provided is not valid", fg="red")  # Mostra un errore se il link non è valido

def startAudioDownload():
    try:
        ytLink = entry_1.get()  # Ottiene il link inserito
        ytObject = YouTube(ytLink)  # Crea un oggetto YouTube
        audio = ytObject.streams.filter(only_audio=True).first()  # Ottiene solo l'audio
        title.config(text=ytObject.title)  # Aggiorna il titolo con il titolo del video
        finishlabel.config(text="")  # Reset dell'etichetta di stato
        audio.download(output_path='audio', filename_prefix='audio_')  # Scarica l'audio nella cartella 'audio'
        finishlabel.config(text="Download finished")  # Aggiorna l'etichetta di stato
    except:
        finishlabel.config(text="The link provided is not valid", fg="red")  # Mostra un errore se il link non è valido

# Buttons for downloading video and audio
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))  # Immagine del pulsante per il download del video
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=startDownload, relief="flat")  # Creazione del pulsante per il download del video
button_1.place(x=38.0, y=276.0, width=333.0, height=106.0)  # Posizionamento del pulsante

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))  # Immagine del pulsante per il download dell'audio
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=startAudioDownload, relief="flat")  # Creazione del pulsante per il download dell'audio
button_2.place(x=400.0, y=276.0, width=333.0, height=106.0)  # Posizionamento del pulsante

# Other images on canvas
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))  # Altra immagine per il canvas
image_1 = canvas.create_image(204.0, 407.0, image=image_image_1)  # Posizionamento dell'immagine
image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))  # Altra immagine per il canvas
image_2 = canvas.create_image(569.0, 407.0, image=image_image_2)  # Posizionamento dell'immagine
image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))  # Altra immagine per il canvas
image_3 = canvas.create_image(38.0, 41.0, image=image_image_3)  # Posizionamento dell'immagine

# Finalize window
window.resizable(False, False)  # Impedisce il ridimensionamento della finestra
window.mainloop()  # Avvia il ciclo principale della GUI
