import customtkinter as ctk


class AboutWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.geometry("400x300")
        self.title("About")
