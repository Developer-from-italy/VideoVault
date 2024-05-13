# Import delle librerie necessarie
from pathlib import Path
import tkinter
from tkinter import Canvas, Entry, Button, PhotoImage

# Import della libreria Pytube per il download dei video da YouTube
from pytube import YouTube
import ssl

# Impostazione del contesto SSL per evitare errori
ssl._create_default_https_context = ssl._create_stdlib_context
ssl._create_default_https_context = ssl._create_unverified_context

# Definizione dei percorsi per l'output e gli asset
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/Users/carlograncini/Developer/VideoVault/build/assets/frame0")

# Funzione per ottenere il percorso relativo agli asset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Inizializzazione della finestra principale di Tkinter
window = tkinter.Tk()

# Impostazione delle dimensioni e del colore di sfondo della finestra
window.geometry("1200x700")
window.configure(bg="#2B2D42")

# Creazione di un canvas all'interno della finestra
canvas = Canvas(
    window,
    bg="#2B2D42",
    height=700,
    width=1200,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

# Posizionamento del canvas nella finestra
canvas.place(x=0, y=0)

# Disegno di un rettangolo nella parte superiore del canvas
canvas.create_rectangle(
    0.0,
    0.0,
    1200.0,
    100.0,
    fill="#EDF2F4",
    outline="")

# Creazione di un testo all'interno del canvas
canvas.create_text(
    424.0,
    26.0,
    anchor="nw",
    text="VideoVault",
    fill="#000000",
    font=("MesloLGS NF Regular", 35 * -1)
)

# Caricamento di un'immagine per l'entry
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    600.0,
    230.0,
    image=entry_image_1
)

# Creazione di un entry widget per inserire il link del video
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=53.0,
    y=188.0,
    width=1094.0,
    height=82.0
)

# Funzione per avviare il download del video
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishlabel.configure(text="")

        video.download()
        finishlabel.configure(text="Download finished")
    except:
        finishlabel.configure(text="The link provided is not valid", text_color="red")

# Funzione per avviare il download dell'audio
def startAudioDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        audio = ytObject.streams.filter(only_audio=True).first()

        title.configure(text=ytObject.title, text_color="white")
        finishlabel.configure(text="")

        audio.download(output_path='audio', filename_prefix='audio_')
        finishlabel.configure(text="Download finished")
    except:
        finishlabel.configure(text="The link provided is not valid", text_color="red")

# Funzione di callback per aggiornare la barra di avanzamento del download
def on_progress(stream, chunk, bytes_remaining):
    tot_size = stream.filesize
    bytes_downloaded = tot_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / tot_size * 100
    perprint = str(int(percentage_of_completion))
    pPercentage.configure(text=perprint + "%")
    pPercentage.update()
    progressBar.set(float(percentage_of_completion) / 100)

# Etichetta per inserire il link del video
title = tkinter.Label(window, text="Insert the link of the video", bg="#2B2D42", fg="white", font=("Helvetica", 16))
title.place(x=53, y=160)

# Entry per il link del video
link = tkinter.StringVar()
link_entry = Entry(window, textvariable=link, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
link_entry.place(x=53, y=210, width=1094, height=50)

# Pulsanti per avviare il download del video e dell'audio
button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
download_button = Button(window, image=button_image_1, borderwidth=0, highlightthickness=0, command=startDownload)
download_button.place(x=155, y=415, width=376, height=115)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
audio_button = Button(window, image=button_image_2, borderwidth=0, highlightthickness=0, command=startAudioDownload)
audio_button.place(x=689, y=404, width=367, height=126)

# Etichette per visualizzare lo stato del download
finishlabel = tkinter.Label(window, text="", bg="#2B2D42", fg="white", font=("Helvetica", 16))
finishlabel.place(x=53, y=530)

pPercentage = tkinter.Label(window, text="0%", bg="#2B2D42", fg="white", font=("Helvetica", 16))
pPercentage.place(x=600, y=550)

# Barra di avanzamento del download
progressBar = Canvas(window, bg="#2B2D42", width=400, height=10, bd=0, highlightthickness=0)
progressBar.place(x=400, y=600)

# Impedisci il ridimensionamento della finestra
window.resizable(False, False)

# Esegui il ciclo principale di Tkinter per mantenere la finestra aperta
window.mainloop()

