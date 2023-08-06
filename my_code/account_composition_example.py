import pdb
import random



# account1 = account(1234, 'IDR')
# pdb.set_trace()

# from src.util.dbHelper import DBHelper #example, normally we would import it
# example of inheritance
class AuthHelper():
    pass

class Account(DatabaseHelper):
    def __init__(self, user_id,database_address, username, password, currency='IDR'):
        super().__init__(database_address, username, password)
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_database()
        print(f'Current balance is : {self.current_balance}')
        self.auth=AuthHelper

    def withdraw(self, amount):
        self.current_balance = self.current_balance - float(amount)
        print(f' ur balance after withdraw is : {self.current_balance}')

    def deposit(self, amount):
        self.current_balance = self.current_balance + float(amount)
        print(f' ur balance after deposit is : {self.current_balance}')

    def generate_statement(self, start_date, end_date):
        pass

    def __read_balance_from_database(self):
        self.read_from_db()
        print(f'Getting balance from db for user : {self.user_id}')
        return random.randint(100, 1000)

    def __write_balance_to_db(self):
        self.write_to_db()
        print(f'saving to db')
class DatabaseHelper():

    def __init__(self, database_address, username, password):
        self.connection = 'just connected'

    def write_to_db(self):
        print('writing..')

    def read_from_db(self):
        print('read..')
#xample of composition
class Account():
    def __init__(self, user_id,database_address, username, password, currency='IDR'):
        self.user_id = user_id
        self.currency = currency
        self.current_balance = self.__read_balance_from_database()
        print(f'Current balance is : {self.current_balance}')
        self.db_helper=DatabaseHelper

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
        self.db_helper.read_from_db()
        return random.randint(100, 1000)

    def __write_balance_to_db(self):
        print(f'saving to db')
        self.db_helper.write_to_db()