import whisper
import pytube
import os

def save_text_in_file(text: str) -> None:
    with open("transcription.txt", "w") as file:
        file.write(text)

def from_youtube(model: whisper.Whisper) -> None:
    url = input("Ingrese la URL del video: ")

    print("Descargando...")
    youtubeVideo = pytube.YouTube(url)
    audio = youtubeVideo.streams.get_audio_only()
    audio.download(filename="tmp.mp4")
    print("Descarga finalizada...")

    print("Convirtiendo...")
    result = model.transcribe("tmp.mp4")
    print("Conversión finalizada...")

    print("Guardando en archivo...")
    save_text_in_file(result["text"])
    print("Guardado finalizado...")
    input("Presiona enter para cerrar el programa...")

def from_local(model: whisper.Whisper) -> None:
    path = input("Ingrese la ruta del archivo: ")
    if(os.path.exists(path)):
        print("Convirtiendo...")
        result = model.transcribe(path)
        print("Conversión finalizada...")

        print("Guardando en archivo...")
        save_text_in_file(result["text"])
        print("Guardado finalizado...")
        input("Presiona enter para cerrar el programa...")

    else:
        print("El archivo no existe...")
        exit(0)

def other_option() -> None:
    print("Saliendo...")
    exit(0)

def main() -> None:
    print("Ingrese una de las siguientes opciones:")
    print("1. Desde YouTube")
    print("2. Archivo local")
    print("3. Salir")
    option = int(input("Opción: "))
    print("Cargando modelo...")
    model = whisper.load_model("small")
    print("Modelo cargado...")
    if(option == 1):
        from_youtube(model)

    elif(option == 2):
        from_local(model)

    else:
        other_option()

if __name__ == "__main__":
    main()
