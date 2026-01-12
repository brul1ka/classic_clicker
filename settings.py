import customtkinter as ctk
import os


class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.geometry("500x400")
        self.resizable(False, False)
        self.title("Settings")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.appearance_label = ctk.CTkLabel(self, text="Appearance mode:")
        self.appearance_label.grid(row=0, column=0, padx=10, pady=20)
        self.appearance_optionmenu = ctk.CTkOptionMenu(
            self, values=["Dark", "Light"], command=self.change_appearance_mode
        )
        self.appearance_optionmenu.grid(row=0, column=1, pady=20)

        self.start_new_game_button = ctk.CTkButton(
            self,
            text="Start new game (delete your save file!!)",
            command=self.delete_save_file,
        )
        self.start_new_game_button.grid(
            row=1, column=0, padx=10, pady=(0, 20), sticky="ew"
        )

    def change_appearance_mode(self, choice):
        (
            ctk.set_appearance_mode("light")
            if choice == "Light"
            else ctk.set_appearance_mode("dark")
        )

    def delete_save_file(self):
        try:
            base_path = os.path.dirname(os.path.realpath(__file__))
            save_path = os.path.join(base_path, "save.json")
            os.remove(save_path)
            self.start_new_game_button.configure(text="Save file deleted. Restart app")
        except FileNotFoundError:
            original_text_on_button = self.start_new_game_button.cget("text")
            self.start_new_game_button.configure(text="But there is no save file!")
            self.after(
                1000,
                lambda: self.start_new_game_button.configure(
                    text=original_text_on_button
                ),
            )
