import customtkinter as ctk

class ClickerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.points = 0

        self.geometry("600x450")
        self.title("Classic Clicker")
        self.columnconfigure(0, weight=1)

        self.your_points_label = ctk.CTkLabel(self, text=f"Your points: {self.points}",font=("Arial", 24))
        self.your_points_label.grid(row=0, column=0, padx=20, pady=(20, 60), sticky="w")
        self.button = ctk.CTkButton(self, text="", width=200, height=200, corner_radius=100, border_width=3, hover_color="#3B4482", command=self.update_points)
        self.button.grid(row=1,column=0)

    def update_points(self):
        self.points = self.points + 1
        self.your_points_label.configure(text=f"Your points: {self.points}")


if __name__ == "__main__":
    app = ClickerApp()
    app.mainloop()