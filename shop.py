import customtkinter as ctk


class ShopWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.button_list = []
        self.spare_price = 300
        self.total_price_for_spares = 0

        self.geometry("500x450")
        self.title("Robot shop")

        self.shop_title = ctk.CTkLabel(
            self, text="Welcome in Robot Shop!", font=("Arial", 32, "bold")
        )
        self.shop_title.pack(pady=(10, 20))

        for i, robot in enumerate(self.master.robots):
            button = ctk.CTkButton(
                self,
                text=f"Buy {robot.name}, price: {robot.price}, gives {robot.power} points in sec. Quantity: {robot.count}",
            )
            button.configure(command=lambda r=robot, b=button: self.buy_robot(r, b))
            button.pack(fill="x", pady=5, padx=20)
            self.button_list.append((button, robot))

        self.spare_button = ctk.CTkButton(
            self,
            text=f"Buy spares for robots repair.\nWhen robot is broken, he gives 1% of his power.\nPrice: {self.spare_price} (for one robot)\n Totally: {self.total_price_for_spares}",
            command=self.buy_spares,
        )
        self.spare_button.pack(fill="x", pady=(50, 0), padx=20)
        self.button_list.append((self.spare_button, "spare"))

        self.update_buttons()

    def buy_robot(self, robot, button):
        if self.master.points >= robot.price:
            self.master.points -= robot.price
            robot.exists = True
            robot.count += 1
            robot.price = int(robot.price * 1.15)

            self.master.your_points_label.configure(
                text=f"Your points:\n{self.master.points}"
            )
            button.configure(
                text=f"Buy spares for robots repair.\nWhen robot is broken, he gives 1% of his power.\nPrice: {self.spare_price} (for one robot)\n Totally: {self.total_price_for_spares}",
            )

    def buy_spares(self):
        if self.master.points >= self.total_price_for_spares:
            self.master.points -= self.total_price_for_spares
            for robot in self.master.robots:
                robot.is_broken = False

    def update_buttons(self):
        for btn, data in self.button_list:
            if data == "spare":
                is_affordable = self.master.points >= self.total_price_for_spares
                for robot in self.master.robots:
                    if robot.is_broken:
                        self.total_price_for_spares += self.spare_price * robot.count

                btn.configure(
                    fg_color="green" if is_affordable else "red",
                    hover_color="dark green" if is_affordable else "dark red",
                    text=f"Buy spares for robots repair.\nWhen robot is broken, he gives 1% of his power.\nPrice: {self.spare_price} (for one robot)\n Totally: {self.total_price_for_spares}",
                )
                self.total_price_for_spares = 0
            else:
                robot = data
                is_affordable = self.master.points >= robot.price
                btn.configure(
                    fg_color="green" if is_affordable else "red",
                    hover_color="dark green" if is_affordable else "dark red",
                )
        self.after(500, self.update_buttons)
