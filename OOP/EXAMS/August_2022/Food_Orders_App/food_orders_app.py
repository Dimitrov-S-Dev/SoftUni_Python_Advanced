from OOP.EXAMS.August_2022.Food_Orders_App.client import Client
from OOP.EXAMS.August_2022.Food_Orders_App.meals.meal import Meal


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def register_client(self, client_phone_number: str):

        if self.__find_client_by_phone_number(client_phone_number):
            raise Exception(f"The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):

        for meal in meals:
            if meal.__class__.__name__ not in ["Starter", "MainDish", "Dessert"]:
                continue
            self.menu.append(meal)

    def show_menu(self):

        self.__check_if_menu_is_ready()
        output = ""
        for meal in self.menu:
            output += meal.details() + "\n"
        return output.strip()
        # second upload

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__check_if_menu_is_ready()

        client = self.__find_client_by_phone_number(client_phone_number)
        if client is None:
            self.register_client(client_phone_number)
            client = self.__find_client_by_phone_number(client_phone_number)

        for meal_name, quantity in meal_names_and_quantities.items():
            if meal_name not in [m.name for m in self.menu]:
                raise Exception(f"{meal_name} is not on the menu!")
            curr_meal = self.__find_meal_by_meal_name(meal_name)
            if quantity > curr_meal.quantity:
                raise Exception(f"Not enough quantity of {curr_meal.__class__.__name__}: {meal_name}!")

        for meal_name, quantity in meal_names_and_quantities.items():
            curr_meal = self.__find_meal_by_meal_name(meal_name)
            client.shopping_cart.append(curr_meal)
            if meal_name not in client.sub_order:
                client.sub_order[meal_name] = 0
            client.sub_order[meal_name] += quantity
            client.bill += curr_meal.price * quantity
            curr_meal.quantity -= quantity
            client.meals_names.append(meal_name)

        return f"Client {client.phone_number} successfully ordered {', '.join(client.meals_names)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):

        client = self.__find_client_by_phone_number(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        for name, quantity in client.sub_order.items():
            cur_meal = self. __find_meal_by_meal_name(name)
            cur_meal.quantity += quantity

        client.shopping_cart = []
        client.bill = 0.0
        client.sub_order = {}
        client.meals_names = []
        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        self.receipt_id += 1
        total_paid_money = client.bill
        client.shopping_cart = []
        client.bill = 0.0
        client.sub_order = {}
        client.meals_names = []
        return f"Receipt #{self.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for " \
               f"{client.phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def __find_client_by_phone_number(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client
        return None

    def __check_if_menu_is_ready(self):
        if len(self.menu) < 5:
            raise Exception(f"The menu is not ready!")

    def __find_meal_by_meal_name(self, name):
        for meal in self.menu:
            if meal.name == name:
                return meal
        raise Exception(f"{name} is not on the menu!")
