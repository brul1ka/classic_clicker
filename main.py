import customtkinter as ctk
from shop import ShopWindow
from entities import Robot


class ClickerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.shop = None
        self.points = 0
        self.points_per_click = 1
        self.price_for_upgrade = 10
        self.robots = [
            Robot("Beginner", 1, 200, False, 0),
            Robot("Clapon", 3, 1000, False, 0),
        ]
        self.income_from_robots = 0

        self.geometry("700x450")
        self.title("Classic Clicker")
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(4, weight=1)

        self.load_save()

        self.your_points_label = ctk.CTkLabel(
            self, text=f"Your points:\n{self.points}", font=("Arial", 24)
        )
        self.your_points_label.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        self.main_button = ctk.CTkButton(
            self,
            text="",
            width=200,
            height=200,
            corner_radius=100,
            border_width=3,
            command=self.update_points,
        )
        self.main_button.grid(row=1, column=1, pady=(0, 50))
        self.upgrade_button = ctk.CTkButton(
            self,
            text=f"Upgrade button (Cost: {self.price_for_upgrade})",
            command=self.upgrade_main_button,
        )
        self.upgrade_button.grid(row=2, column=1)
        self.shop_button = ctk.CTkButton(
            self,
            text="S\nH\nO\nP",
            command=self.open_shop,
            height=250,
            font=("Arial", 28),
        )
        self.shop_button.grid(row=1, column=2, padx=10, rowspan=2, sticky="e")
        self.about_button = ctk.CTkButton(self, text="About")
        self.about_button.grid(row=5, column=0, padx=20, pady=5, sticky="sw")
        self.settings_buttton = ctk.CTkButton(self, text="Settings")
        self.settings_buttton.grid(row=6, column=0, padx=20, pady=(5, 20), sticky="sw")
        self.your_robots_label = ctk.CTkLabel(self)
        self.your_robots_label.grid(row=6, column=2, sticky="ew")

        self.auto_click()

    def update_points(self):
        self.points = self.points + self.points_per_click
        self.your_points_label.configure(text=f"Your points:\n{self.points}")

    def upgrade_main_button(self):
        if self.points >= self.price_for_upgrade:
            self.points -= self.price_for_upgrade
            self.points_per_click += 1
            self.price_for_upgrade *= 10

            self.your_points_label.configure(text=f"Your points:\n{self.points}")
            self.upgrade_button.configure(
                text=f"Upgrade button (Cost: {self.price_for_upgrade})"
            )

            self.save_game()

    def open_shop(self):
        if self.shop == None or not self.shop.winfo_exists():
            self.shop = ShopWindow(self)
        else:
            self.shop.focus()

    def save_game(self):
        with open("save.txt", "w") as file:
            file.write(str(self.points) + "\n")
            file.write(str(self.points_per_click) + "\n")
            file.write(str(self.price_for_upgrade) + "\n")
            for robot in self.robots:
                file.write(str(1) + "\n") if robot.exists else file.write(str(0) + "\n")
                file.write(str(robot.how_many) + "\n")

    def on_closing(self):
        self.save_game()
        self.destroy()

    def load_save(self):
        try:
            with open("save.txt", "r") as file:
                lines = file.readlines()
                try:
                    if len(lines) >= 3:
                        self.points = int(lines[0])
                        self.points_per_click = int(lines[1])
                        self.price_for_upgrade = int(lines[2])

                        if len(lines) >= 4:
                            for i, robot in enumerate(self.robots):
                                robot.exists = bool(int(lines[3 + i]))
                                robot.how_many = int(lines[4 + i])
                except ValueError:
                    print(
                        "ERROR: something isn't integer in save.txt, restoring to default values"
                    )
                    self.points = 0
                    self.points_per_click = 1
                    self.price_for_upgrade = 10
        except FileNotFoundError:
            print("INFO: no save file")

    def auto_click(self):
        for i, robot in enumerate(self.robots):
            if robot.exists:
                self.income_from_robots += robot.power * robot.how_many

        self.points += self.income_from_robots
        self.your_points_label.configure(text=f"Your points:\n{self.points}")
        self.your_robots_label.configure(
            text=f"Power of all your robots: {self.income_from_robots}"
        )
        self.income_from_robots = 0
        self.after(1000, self.auto_click)


if __name__ == "__main__":
    app = ClickerApp()
    app.mainloop()
