from user.user import User
from shop.list import PetList


import datetime
import mysql.connector


customer = User()


class Enter:
    def enters(self):
        # Check if the user wants to buy a pet
        buy_pet = input("Do you want to buy a pet? (y/n): ")
        if buy_pet.lower() == "y":
            customer.log_in()

            # Process payment
            customer.log_out()
        choice1 = ""
        choice2 = input(
            "Thank You for our visit. Press '1' to quit\nPress Enter to Login\n"
        )

        if choice2 != choice1:
            raise SystemExit
        else:
            customer.log_in()


class Welcome:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host="127.0.0.15",
            user="root",
            password="root",
            database="pet_adoption",
        )

    def save_timestamp(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor = self.db_connection.cursor()
        cursor.execute("USE pet_adoption")
        print("Using pet_adoption Database")

        query = """CREATE TABLE IF NOT EXISTS timestamp_login (id INT AUTO_INCREMENT PRIMARY KEY, timestamp DATETIME)"""
        cursor.execute(query)
        print("Table Created")

        query = "INSERT INTO timestamp_login (timestamp) VALUES (%s)"
        values = (timestamp,)
        cursor.execute(query, values)
        self.db_connection.commit()
        cursor.close()

    def display_welcome_screen(self):
        print("Welcome to Adams Pet Shop!")
        self.save_timestamp()
        customer.create_account()


Welcome().display_welcome_screen()
