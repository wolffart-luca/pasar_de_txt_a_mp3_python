import pyttsx3
from pydub import AudioSegment

def text_to_speech(text, output_file):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

# Aqui lee el contenido del archivo
with open("nombre_del_archivo_de_texto.txt", "r", encoding="utf-8") as book:
    book_text = book.read()

# Aqui se convierte el texto a voz y guarda el archivo de salida como MP3
output_file = "nombre_del_archivo_saliente.mp3"
text_to_speech(book_text, output_file)

print("Archivo MP3 guardado correctamente.")