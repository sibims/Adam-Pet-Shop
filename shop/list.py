import mysql.connector

from shop.booking import Booking

booking = Booking()


class PetList:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host="127.0.0.15",
            user="root",
            password="root",
            database="pet_adoption",
        )

    def display_pet_list(self):
        # Fetch the list of available pets from the database and display them
        cursor = self.db_connection.cursor()

        create_table_query = """CREATE TABLE IF NOT EXISTS pets (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),breed VARCHAR(50),age INT,gender VARCHAR(10),temperament VARCHAR(50),status VARCHAR(20))"""
        cursor.execute(create_table_query)

        query = "SELECT id, name, breed, age, gender, temperament, status FROM pets WHERE status = 'Available'"
        cursor.execute(query)
        pets = cursor.fetchall()

        print("List of available pets:")
        for pet in pets:
            print(
                f"ID: {pet[0]}, Name: {pet[1]}, Breed: {pet[2]}, Age: {pet[3]}, Gender: {pet[4]}, Temperament: {pet[5]}, Status: {pet[6]}"
            )
        ret = input("Want to book a date?[y/n]: ")
        if ret == "y":
            booking.select_date()
            return

        cursor.close()
        return
