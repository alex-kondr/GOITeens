import os
from tkinter import Tk, Button, Label, filedialog, Scale, HORIZONTAL
from PIL import Image
from pydub import AudioSegment


# Потрібно розробити систему, яка використовує
# сучасні методи стиснення даних для зменшення
# розміру текстур та аудіо файлів у відеоіграх.


def compress_image(input_path, output_path, quality=50):
    img = Image.open(input_path)
    img.save(output_path, 'JPEG', quality=quality)
    return os.path.getsize(output_path)


def compress_audio(input_path, output_path, bitrate="64k"):
    audio = AudioSegment.from_file(input_path)
    audio.export(output_path, format="mp3", bitrate=bitrate)
    return os.path.getsize(output_path)


def select_and_compress_image():
    input_path = filedialog.askopenfilename(title="Виберіть зображення", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if not input_path:
        return

    output_path = filedialog.asksaveasfilename(title="Зберегти стиснене зображення", defaultextension=".jpg", filetypes=[("JPEG", "*.jpg")])
    if not output_path:
        return

    quality = quality_scale.get()
    original_size = os.path.getsize(input_path)
    new_size = compress_image(input_path, output_path, quality=quality)
    result_label.config(text=f"Зображення стиснене.\nОригінальний розмір: {original_size/1024:.2f} KB\nНовий розмір: {new_size/1024:.2f} KB")


def select_and_compress_audio():
    input_path = filedialog.askopenfilename(title="Виберіть аудіофайл", filetypes=[("Audio Files", "*.wav;*.mp3;*.ogg")])
    if not input_path:
        return
    output_path = filedialog.asksaveasfilename(title="Зберегти стиснене аудіо", defaultextension=".mp3", filetypes=[("MP3", "*.mp3")])
    if not output_path:
        return

    bitrate = "64k"
    original_size = os.path.getsize(input_path)
    new_size = compress_audio(input_path, output_path, bitrate=bitrate)
    result_label.config(text=f"Аудіо стиснене.\nОригінальний розмір: {original_size/1024:.2f} KB\nНовий розмір: {new_size/1024:.2f} KB")


root = Tk()
root.title("Оптимізація Завантаження Ресурсів у Іграх")
root.geometry("450x350")

instruction_label = Label(root, text="Оберіть ресурс для стиснення:", font=("Arial", 12))
instruction_label.pack(pady=10)

image_button = Button(root, text="Стиснення Зображення", width=25, command=select_and_compress_image)
image_button.pack(pady=5)

audio_button = Button(root, text="Стиснення Аудіо", width=25, command=select_and_compress_audio)
audio_button.pack(pady=5)

quality_scale = Scale(root, from_=10, to=100, orient=HORIZONTAL, label="Якість зображення (JPEG)")
quality_scale.set(50)
quality_scale.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 10))
result_label.pack(pady=10)

root.mainloop()
