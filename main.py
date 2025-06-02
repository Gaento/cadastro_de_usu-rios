import re
import mysql.connector
from random import randint

class User:
    def __init__(self, name, email, telephone, user_id=None):
        self.name = name
        self.email = email
        self.telephone = telephone
        self.id = user_id if user_id else randint(1000, 5000)

    def __str__(self):
        return f'{self.id} | {self.name} | {self.email} | {self.telephone}'


class UserManager:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="",
            user="",
            password="",
            database=""
        )
        self.cursor = self.db.cursor()

    def Create(self):
        formE = r"^[\w\.]+@gmail\.com$"
        formT = r"^\d{2} \d{5}-\d{4}$"
        name = input("What's your name? ").lower().title()

        email = input("What's your email? ").lower()
        while not re.fullmatch(formE, email):
            print("Invalid email.")
            email = input("What's your email? ").lower()

        telephone = input("Write your telephone: e.g(xx xxxxx-xxxx) ")
        while not re.fullmatch(formT, telephone):
            print("Invalid telephone.")
            telephone = input("Write your telephone: e.g(xx xxxxx-xxxx) ")

        user = User(name, email, telephone)

        self.cursor.execute(
            "INSERT INTO users (id, name, email, telephone) VALUES (%s, %s, %s, %s)",
            (user.id, user.name, user.email, user.telephone)
        )
        self.db.commit()
        print(f'User registered: {user}')

    def user_list(self):
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()

        if not users:
            print("No users found.")
            return

        for i, user in enumerate(users, 1):
            print(f"[{i}] {user[0]} | {user[1]} | {user[2]} | {user[3]}")

    def Delete(self):
        self.user_list()
        try:
            user_id = int(input("Which ID do you want to delete? "))
        except ValueError:
            print("Invalid ID.")
            return

        self.cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        self.db.commit()

        if self.cursor.rowcount == 0:
            print("User not found.")
        else:
            print("User deleted.")

    def Update(self):
        formE = r"^[\w\.]+@gmail\.com$"
        formT = r"^\d{2} \d{5}-\d{4}$"

        try:
            user_id = int(input("Enter the ID of the user to update: "))
        except ValueError:
            print("Invalid ID.")
            return

        self.cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = self.cursor.fetchone()

        if not user:
            print("User not found.")
            return

        try:
            opt = int(input("[1] Name\n[2] Email\n[3] Telephone\nChoose: "))
        except ValueError:
            print("Invalid option.")
            return

        if opt == 1:
            new_name = input("New name: ").title()
            self.cursor.execute("UPDATE users SET name = %s WHERE id = %s", (new_name, user_id))

        elif opt == 2:
            new_email = input("New email: ")
            while not re.fullmatch(formE, new_email):
                print("Invalid format.")
                new_email = input("New email: ")
            self.cursor.execute("UPDATE users SET email = %s WHERE id = %s", (new_email, user_id))

        elif opt == 3:
            new_telephone = input("New telephone: ")
            while not re.fullmatch(formT, new_telephone):
                print("Invalid format.")
                new_telephone = input("New telephone: ")
            self.cursor.execute("UPDATE users SET telephone = %s WHERE id = %s", (new_telephone, user_id))

        else:
            print("Invalid choice.")
            return

        self.db.commit()
        print("User updated successfully.")

    def Menu(self):
        print("=== User Management System (MySQL) ===")
        while True:
            print("\n[1] Create\n[2] Update\n[3] Delete\n[4] List\n[5] Exit\n")
            try:
                option = int(input("Choose: "))
            except ValueError:
                print("Invalid option.")
                continue

            if option == 1:
                self.Create()
            elif option == 2:
                self.Update()
            elif option == 3:
                self.Delete()
            elif option == 4:
                self.user_list()
            elif option == 5:
                print("Exiting...")
                break
            else:
                print("Choose from 1 to 5.")


if __name__ == "__main__":
    manager = UserManager()
    manager.Menu()
