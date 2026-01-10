import customtkinter as ctk

class ShopWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("300x200")
        self.title("Shop")

        header = ctk.CTkLabel(self, text="Welcome to the shop!")
        header.grid(row=0, column=0)