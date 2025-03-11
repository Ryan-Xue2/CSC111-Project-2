"""This module helps manager account data"""
from typing import Optional
import json
from dataclasses import dataclass
from helper import Helper


@dataclass
class User:
    """A user class storing all useful login/registeration functions for quick referral.

    Instance Attributes:
        - name: A string of the name of user:
        - password: A string of the password of user
    """

    name: str
    password: str


class Accounts:
    """A manager class for user accounts"""
    _accounts: dict[str, User]

    def __init__(self, data_file: str) -> None:
        """Initialize accounts by reading data from appropriate account file"""
        self._accounts = self.load(data_file)

    @staticmethod
    def load(account_file: str) -> dict[str, User]:
        """Load account data from json data file"""

        with open(account_file, "r") as file:
            account_data = json.load(file)

        user_dict = {}

        for account in account_data:
            user_obj = User(account, account_data[account]["password"])
            user_dict[account] = user_obj

        return user_dict

    def get_account(self, name: Optional[str] = None) -> dict[str, User] | User:
        """An accessor method used to access account object"""

        if name is None:
            return self._accounts
        else:
            return self._accounts[name]

    def login(self, name: str, password: str) -> bool:
        """Check if name and passsword entered by user is the same as account info in database"""
        if name in self._accounts and password == self._accounts[name].password:
            return True
        else:
            return False

    def register(self, name: str, password: str) -> None:
        """Register a new account into the database with initial default game data"""

        self._accounts[name] = User(name, password)

        account_data = {}
        for account in self._accounts:
            data = self._accounts[account]
            account_data[account] = {"password": data.password}

        with open("account_data.json", "w") as f:
            json.dump(account_data, f, indent=2)

    def handle_login(self) -> User | None:
        """A function to help manage the prompt message for user account info，
        Return user oject containing user info"""
        login = False
        user = None

        if not login:
            choice = input("Would you like to login or register [login/register]: ").strip().lower()

            while choice not in ["login", "register"]:
                print(choice, "is not a valid input. \n")
                choice = input("Try again [login/register]: ")

            if choice == "login":

                print("Please enter your username and password [case sensitive]")

                username = input("Username: ").strip()
                password1 = input("Password: ").strip()

                while not self.login(username, password1):

                    print("Username or password was incorrect, please try again.")
                    username = input("Username: ").strip()
                    password1 = input("Password: ").strip()

                user = self.get_account()[username]

                login = True

            elif choice == "register":
                print("Please enter your username and password [case sensitive]")
                username = input("Username: ").strip()

                while username in self.get_account():
                    print("Username taken, please try again.")
                    username = input("Username: ").strip()

                password1 = input("Password: ").strip()
                password2 = input("Enter password again: ").strip()

                while password1 != password2:

                    print("Passwords do not match, please try again.")

                    password1 = input("Password: ").strip()
                    password2 = input("Enter password again: ").strip()

                self.register(username, password1)
                user = self.get_account()[username]

                login = True

        return user


if __name__ == "__main__":
    # pass
    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    # IMPORTANT: keep this code indented inside the "if __name__ == '__main__'" block
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['R1705', 'E9998', 'E9999']
    })
