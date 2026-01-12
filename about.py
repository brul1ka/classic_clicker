import customtkinter as ctk
import os
from PIL import Image
import webbrowser


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

        left_frame = ctk.CTkFrame(self, fg_color="transparent")
        left_frame.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        base_path = os.path.dirname(os.path.realpath(__file__))
        logo_path = os.path.join(base_path, "res", "logo.png")
        self.logo = ctk.CTkImage(
            Image.open(logo_path), Image.open(logo_path), (150, 150)
        )
        self.logo_image = ctk.CTkLabel(left_frame, image=self.logo, text="")
        self.logo_image.pack(pady=(0, 10))

        self.about = ctk.CTkLabel(
            self,
            text=description_text,
            justify="left",
            wraplength=200,
        )
        self.about.grid(row=0, column=1, padx=(0, 10), pady=20)
        self.github_button = ctk.CTkButton(
            left_frame,
            text="My project on GitHub!",
            fg_color="#24292e",
            hover_color="#404448",
            width=150,
            command=lambda: webbrowser.open_new_tab(
                "https://github.com/brul1ka/classic-clicker"
            ),
        )
        self.github_button.pack()
