import json
import random
import string
from pathlib import Path


class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An exception occurs as {err}")

    @staticmethod
    def update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    def createaccount(self):
        data = {
            "name": input("What is your Name: "),
            "age": int(input("What is your Age: ")),
            "email": input("Write email: "),
            "pin": int(input("Write your 4 numbers pin code: ")),
            "accountNo.": 1234,
            "balance": 0
        }
        if data['age'] < 18 or len(str(data['pin'])) != 4:
            print("Sorry you cannot create your account")
        else:
            print("Account has been created successfully")
            for i in data:
                print(f"{i} : {data[i]}")
            print("note down your account number")

            Bank.data.append()

            Bank.update(data)


user = Bank()

print("Press 1 for Creating an Account")
print("Press 2 for Deposite the money in the Bank")
print("Press 3 for withdraw the money")
print("Press 4 for Deteils")
print("Press 5 to Update the Details")
print("Press 6 for Delete the Account")

check = int(input("Tell your response here: "))

if  check == 1:
    user.createaccount()
