import customtkinter as ctk


class ShopWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.button_list = []

        self.geometry("500x450")
        self.title("Robot shop")

        for i, robot in enumerate(self.master.robots):
            button = ctk.CTkButton(
                self,
                text=f"Buy {robot.name}, price: {robot.price}, gives {robot.power} points in sec",
            )
            button.configure(command=lambda r=robot, b=button: self.buy_robot(r, b))
            button.pack(fill="x", pady=15, padx=20)
            self.button_list.append((button, robot))

        self.update_buttons()

    def buy_robot(self, robot, button):
        if self.master.points >= robot.price:
            self.master.points -= robot.price
            robot.exists = True
            self.master.your_points_label.configure(
                text=f"Your points: {self.master.points}"
            )

    def update_buttons(self):
        for btn, robot in self.button_list:
            btn.configure(
                hover_color=(
                    "dark green" if self.master.points >= robot.price else "dark red"
                ),
                fg_color="green" if self.master.points >= robot.price else "red",
            )
        self.after(100, self.update_buttons)
