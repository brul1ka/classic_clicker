import customtkinter as ctk

class ShopWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("300x200")
        self.title("Shop")

        header = ctk.CTkLabel(self, text="Welcome to the shop!")
        header.grid(row=0, column=0)



class ClickerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.shop = None
        self.points = 0
        self.points_per_click = 1
        self.price_for_upgrade = 10

        self.geometry("600x450")
        self.title("Classic Clicker")
        self.columnconfigure(0, weight=1)

        self.your_points_label = ctk.CTkLabel(self, text=f"Your points: {self.points}",font=("Arial", 24))
        self.your_points_label.grid(row=0, column=0, padx=20, pady=(20, 60), sticky="w")
        self.main_button = ctk.CTkButton(self, text="", width=200, height=200, corner_radius=100, border_width=3, hover_color="#3B4482", command=self.update_points)
        self.main_button.grid(row=1, column=0, pady=(0,50))
        self.upgrade_button = ctk.CTkButton(self, text=f"Upgrade button (Cost: {self.price_for_upgrade})", command=self.upgrade_main_button)
        self.upgrade_button.grid(row=2, column=0)
        self.shop_button = ctk.CTkButton(self, text="To the shop", command=self.open_shop)
        self.shop_button.grid(row=1, column=1)

    def update_points(self):
        self.points = self.points + self.points_per_click
        self.your_points_label.configure(text=f"Your points: {self.points}")

    def upgrade_main_button(self):
        if self.points >= self.price_for_upgrade:
            self.points -= self.price_for_upgrade
            self.your_points_label.configure(text=f"Your points: {self.points}")
            self.points_per_click += 1
            self.price_for_upgrade *= 10
            self.upgrade_button.configure(text=f"Upgrade button (Cost: {self.price_for_upgrade})")

    def open_shop(self):
        if self.shop == None or not self.shop.winfo_exists():
            self.shop = ShopWindow(self)
        else:
            self.shop.focus()

if __name__ == "__main__":
    app = ClickerApp()
    app.mainloop()