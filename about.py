import customtkinter as ctk
from PIL import Image


class AboutWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.geometry("400x300")
        self.title("About")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.resizable(False, False)

        description_text = """
Classic Clicker

This is my personal project created to:
* Learn the CustomTkinter library
* Practice Python
* Waste time with maximum benefit

Developed with passion by: brul1ka
Version: idk
        """

        logo = ctk.CTkImage(
            Image.open("res/logo.png"), Image.open("res/logo.png"), (150, 150)
        )
        logo_image = ctk.CTkLabel(self, image=logo, text="")
        logo_image.grid(row=0, column=0, padx=(20, 10), pady=20, sticky="ew")

        about = ctk.CTkLabel(
            self,
            text=description_text,
            justify="left",
            wraplength=200,
        )
        about.grid(row=0, column=1, padx=(0, 10), pady=20)
