import pdb
import random


class account():
    def __init__(self, user_id, currency='IDR'):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_database()
        print(f'Current balance is : {self.current_balance}')

    def withdraw(self, amount):
        self.current_balance = self.current_balance - float(amount)
        print(f' ur balance after withdraw is : {self.current_balance}')
    def deposit(self, amount):
        self.current_balance = self.current_balance + float(amount)
        print(f' ur balance after deposit is : {self.current_balance}')

    def generate_statement(self, start_date, end_date):
        pass

    def __read_balance_from_database(self):
        print(f'Getting balance from db for user : {self.user_id}')
        return random.randint(100, 1000)


account1 = account(1234, 'IDR')
pdb.set_trace()