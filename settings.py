import customtkinter as ctk


class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.geometry("500x400")
        self.resizable(False, False)
        self.title("Settings")

        self.appearance_label = ctk.CTkLabel(self, text="Appearance mode:")
        self.appearance_label.grid(row=0, column=0, padx=20, pady=20)
        self.appearance_optionmenu = ctk.CTkOptionMenu(
            self, values=["Dark", "Light"], command=self.change_appearance_mode
        )
        self.appearance_optionmenu.grid(row=0, column=1, pady=20)

    def change_appearance_mode(self, choice):
        (
            ctk.set_appearance_mode("light")
            if choice == "Light"
            else ctk.set_appearance_mode("dark")
        )
