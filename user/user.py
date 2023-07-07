import mysql.connector
import datetime
import time

from shop.list import PetList

username = ""
logged = ""


class User:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host="127.0.0.15",
            user="root",
            password="root",
            database="pet_adoption",
        )
        cursor = self.db_connection.cursor()
        cursor.execute("USE pet_adoption")

        query = """CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(50) UNIQUE,password VARCHAR(50))"""
        cursor.execute(query)
        self.db_connection.commit()
        self.logged_in = False

    def create_account(self):
        self.create_table_if_not_exists()

        print("Create a new user account:")
        username = input("Enter a username: ")
        if username == "":
            print("Redirecting to Login")
            return

        else:
            password = input("Enter a password: ")
            # Insert the user credentials into the database
            cursor = self.db_connection.cursor()
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            values = (username, password)
            cursor.execute(query, values)
            self.db_connection.commit()
            cursor.close()

            print("Account created successfully!")
        return

    def log_in(self):
        # Implement logic to log in the user and validate the credentials from the database
        self.create_table_if_not_exists()

        print("Log in to your account:")
        ret1 = "0"
        ret2 = input(
            "New to Adam's Shop? Press any key to Create a account\nElse Press '0' to Login\n"
        )

        if ret2 == ret1:
            global username
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            cursor = self.db_connection.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            values = (username, password)
            cursor.execute(query, values)
            user2 = cursor.fetchone()
            cursor.close()
            user1 = ""

            if user2 != user1:
                self.logged_in = True
                print("Login successful!")

                pet_list = PetList()  # Create an instance of the PetList class
                pet_list.display_pet_list()  # Call the display_pet_list method inside PetList
            else:
                print("Invalid username or password!")

            self.logged_in = True
            global logged
            logged = self.logged_in
            return username
        else:
            self.create_account()
            return

    def log_out(self):
        print("Logging out automatically in 5 seconds.....")
        time.sleep(5)

        # Get the current timestamp
        timestamp = datetime.datetime.now()
        global username

        # Insert the log into the database
        cursor = self.db_connection.cursor()

        query = (
            "INSERT INTO timestamp_logout (username, logout_timestamp) VALUES (%s, %s)"
        )
        values = (username, timestamp)
        cursor.execute(query, values)
        self.db_connection.commit()
        cursor.close()

        self.logged_in = False
        print("Logged out successfully!")

    def create_table_if_not_exists(self):
        cursor = self.db_connection.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE,
            password VARCHAR(50)
        )
        """
        cursor.execute(query)

        query = """
        CREATE TABLE IF NOT EXISTS timestamp_logout (
            username VARCHAR(50),
            logout_timestamp DATETIME
        )
        """
        cursor.execute(query)

        self.db_connection.commit()
        cursor.close()
