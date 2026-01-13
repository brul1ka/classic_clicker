import customtkinter as ctk
import json
from dataclasses import asdict
from shop import ShopWindow
from about import AboutWindow
from settings import SettingsWindow
from robot import Robot


class ClickerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.shop = None
        self.settings = None
        self.about = None
        self.points = 0
        self.points_per_click = 1
        self.price_for_upgrade = 10
        self.robots = [
            Robot("Beginner", 1, 200),
            Robot("Clapon", 3, 1000),
            Robot("Sen", 10, 2500),
        ]
        self.income_from_robots = 0

        self.geometry("700x450")
        self.title("classic clicker")
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
        self.shop_button.grid(row=1, column=2, padx=10, sticky="e")
        self.about_button = ctk.CTkButton(self, text="About", command=self.open_about)
        self.about_button.grid(row=5, column=0, padx=20, pady=5, sticky="sw")
        self.settings_buttton = ctk.CTkButton(
            self, text="Settings", command=self.open_settings
        )
        self.settings_buttton.grid(row=6, column=0, padx=20, pady=(5, 20), sticky="sw")
        self.power_of_all_robots_label = ctk.CTkLabel(self, font=("Arial", 16))
        self.power_of_all_robots_label.grid(row=6, column=2, pady=(0, 20), padx=(0, 10))
        self.robot_is_broken_label = ctk.CTkLabel(
            self, text="", font=("Arial", 18), justify="right"
        )
        self.robot_is_broken_label.grid(row=0, column=2, padx=10)

        self.auto_click()
        self.to_breakdown()

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

    def open_about(self):
        if self.about == None or not self.about.winfo_exists():
            self.about = AboutWindow(self)
        else:
            self.about.focus()

    def open_settings(self):
        if self.settings == None or not self.settings.winfo_exists():
            self.settings = SettingsWindow(self)
        else:
            self.settings.focus()

    def save_game(self):
        robots_data = []
        for robot in self.robots:
            dto = robot.to_dto()
            robots_data.append(asdict(dto))

        data_for_save = {
            "points": self.points,
            "points_per_click": self.points_per_click,
            "price_for_upgrade": self.price_for_upgrade,
            "robots": robots_data,
        }

        with open("save.json", "w", encoding="utf-8") as file:
            json.dump(data_for_save, file, indent=4)

    def on_closing(self):
        self.save_game()
        self.destroy()

    def load_save(self):
        try:
            with open("save.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                self.points = data["points"]
                self.points_per_click = data["points_per_click"]
                self.price_for_upgrade = data["price_for_upgrade"]
                robot_list_from_save = data["robots"]
                for i, robot in enumerate(self.robots):
                    if i < len(robot_list_from_save):
                        robot_data = robot_list_from_save[i]
                        robot.exists = robot_data["exists"]
                        robot.count = robot_data["count"]
                        robot.price = robot_data["price"]
                        robot.is_broken = robot_data["is_broken"]
        except FileNotFoundError:
            print("INFO: no save file")
        except KeyError as e:
            print(f"ERROR: Missing key in save file: {e}")

    def auto_click(self):
        for i, robot in enumerate(self.robots):
            if robot.exists:
                multiplier = 1.0 if not robot.is_broken else 0.1
                self.income_from_robots += int(robot.power * robot.count * multiplier)

        self.points += self.income_from_robots
        self.your_points_label.configure(text=f"Your points:\n{self.points}")
        self.power_of_all_robots_label.configure(
            text=f"Power of all your robots: {self.income_from_robots}"
        )
        self.income_from_robots = 0
        self.after(1000, self.auto_click)

    def to_breakdown(self):
        broken_robot_list = []
        for robot in self.robots:
            if robot.check_for_breakdown() or robot.is_broken:
                broken_robot_list.append(robot.name)
        if broken_robot_list:
            names = ", ".join(broken_robot_list)
            self.robot_is_broken_label.configure(
                text=f"{names}\nhave broken down!", text_color="red"
            )
        else:
            self.robot_is_broken_label.configure(text="")

        self.after(1000, self.to_breakdown)


if __name__ == "__main__":
    app = ClickerApp()
    app.mainloop()
