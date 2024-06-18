from tkinter import *
from tkinter import messagebox
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageTk
import pyperclip

class BarcodeGenerator(Tk):
    def __init__(self):
        super().__init__()

        self.title("Barcode Generator")
        self.geometry("400x400")
        self.resizable(0, 0)

        self.input_text = StringVar(self)

        self.create_widgets()

        self.mainloop()

    def generate_barcode(self):
        text = self.input_text.get()
        if not text:
            messagebox.showerror("Error", "Input text cannot be empty!")
            return

        try:
            # Создаем объект штрих-кода
            barcode_class = barcode.get_barcode_class('code128')
            barcode_obj = barcode_class(text, writer=ImageWriter())
            img_path = "barcode.png"
            barcode_obj.save(img_path)

            self.display_barcode(img_path)

            pyperclip.copy(text)
            messagebox.showinfo("Copied", "Your text was copied to the clipboard!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_barcode(self, img_path):
        img = Image.open(img_path)
        img = img.resize((300, 150), Image.LANCZOS)  # Изменяем размер изображения
        img = ImageTk.PhotoImage(img)

        self.barcode_label.config(image=img)
        self.barcode_label.image = img

    def create_widgets(self):
        Label(self, text="Enter text to generate Barcode:").pack(pady=10)

        Entry(self, textvariable=self.input_text, width=50).pack(pady=10)

        Button(self, text="Generate Barcode", command=self.generate_barcode).pack(pady=10)

        self.barcode_label = Label(self)
        self.barcode_label.pack(pady=10)

if __name__ == "__main__":
    BarcodeGenerator()
