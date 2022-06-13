#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:13:01 2022

@author: shrirupdwivedi
"""

import sqlalchemy as db
from sqlalchemy import exc
import sys
import logging


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Creates a logger
logger = logging.getLogger(__name__)

# set logger level
logger.setLevel(logging.DEBUG)

# define file handler and set formatter
file_handler = logging.FileHandler('Bank.log')
formatter = logging.Formatter(
    '%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)
# Create test.sqlite automatically
engine = db.create_engine('sqlite:///test.sqlite')
connection = engine.connect()
metadata = db.MetaData()


Customer = db.Table('Customer', metadata,
                    db.Column('acc_no', db.Integer(), primary_key=True,
                              nullable=False, autoincrement=True),
                    db.Column('first_name', db.String(255), nullable=False),
                    db.Column('last_name', db.String(255)),
                    db.Column('dob', db.Integer()),
                    db.Column('email', db.String(255)),
                    db.Column('acc_type', db.String(255)),
                    db.Column('status', db.String(255)),
                    db.Column('balance', db.Integer())

                    )

metadata.create_all(engine)  # Creates the table


class Sql():

    def execute(self, query):
        return connection.execute(query)

    def fetchall(self, query):
        return connection.execute(query).fetchall()

    def fetchone(self, query):
        return connection.execute(query).fetchone()


class Bank(Sql):

    def __init__(self):

        self.main()
        sql.__init__()

    def create_acc(self):
        
        try:

            self.first_name = input("Enter the account holder first name : \n")
            self.last_name = input("Enter the account holder last name : \n")
            self.dob = int(input("Enter the account holder date of birth : \n"))
            self.email = input("Enter the account holder email: \n")
            self.acc_type = input("Account type (saving/checking): \n")
            self.balance = int(input("Enter opening balance: \n"))
            
    
    
            query = db.insert(Customer).values(first_name=self.first_name, last_name=self.last_name, dob=self.dob,
                                               status='Active', email=self.email, acc_type=self.acc_type,
                                               balance=self.balance)
    
            ResultProxy = self.execute(query)
            query1 = db.select([Customer])
            results = self.fetchall(query1)
            print(results)
    
            print('\n  New customer added successfully!\n\n')
        except ValueError:
            
            print( "\n********\nInvalid input!\n*********\n TypeError. Please try again!\n")

            logger.error("Type Error. Invalid input in create_acc()")
            self.main()
            
 

    def deposit(self):

        self.acc_no = input('Enter your account number: \n')
        self.amount = input('Enter the amount to deposit: \n')
        

        result = self.check_status(self.acc_no)

        try:
            self.amount = int(self.amount)
            if result[0] == 'Active':

                query = Customer.update().values(balance=self.amount+Customer.columns.balance)\
                    .where(db.and_(Customer.columns.acc_no == self.acc_no, Customer.columns.status == 'Active'))
    
                ResultProxy = self.execute(query)
                query1 = db.select([Customer])
                results = self.fetchall(query1)
                print(results)
    
                print('\n  Deposited successfully!\n\n')
            else:

                logger.error("ValueError. Invalid input for the account number: '{}' in close(). Account is closed. in deposit()".format(self.acc_no))
                print("\n*******\nInvalid input!\n*********\n ValueError. The account is already closed. Please try again!\n")
                self.main()
        
           
            self.main()
        except TypeError:
            print( "\n********\nInvalid input!\n*********\n TypeError. Please try again!\n")

            logger.error("Type Error. Invalid input: with the account number:'{}'.in close()".format(self.acc_no))
            
        except ValueError:
            
            print( "\n********\nInvalid input!\n*********\n ValueError with amount. Please try again!\n")

            logger.error("Value Error. Invalid input: with the amount :'{}'.in close()".format(self.acc_no))

    def withdraw(self):

        try:

            self.acc_no = input('Enter your account number: ')
            self.amount = input('Enter the amount to withdraw: ')
            self.amount = int(self.amount)
            result = self.check_status(self.acc_no)

            if result[0] == 'Active':

                query = Customer.update().values(balance=Customer.columns.balance-self.amount)\
                    .where(db.and_(Customer.columns.acc_no == self.acc_no, Customer.columns.status == 'Active'))
            
                ResultProxy = self.execute(query)
                query1 = db.select([Customer])
                results = self.fetchall(query1)
                print(results)

                print('\n   Withdrawl conducted successfully!\n\n')

            else:
                logger.error("ValueError. Invalid input for the account number: '{}' in withdraw(). Account is closed. in deposit()".format(self.acc_no))
                print("\n*******\nInvalid input!\n*********\n ValueError. The account is already closed. Please try again!\n")
                self.main()
        
        except TypeError:
            print( "\n********\nInvalid input!\n*********\n TypeError. Please try again!\n")

            logger.error("Type Error. Invalid input: with the account number:'{}'.in withdraw()".format(self.acc_no))
            
        except ValueError:
            
            print( "\n********\nInvalid input!\n*********\n ValueError with amount. Please try again!\n")

            logger.error("Value Error. Invalid input: with the amount :'{}'.in withdraw()".format(self.acc_no))


    def close(self):
        
        
        self.acc_no = input('Enter the account number of the account to be closed: ')
        result = self.check_status(self.acc_no)
        
        try:
            
            if result[0] == 'Active':
    
                query = Customer.update().values(status='Inactive')\
                    .where(db.and_(Customer.columns.acc_no == self.acc_no, Customer.columns.status == 'Active'))
        
                ResultProxy = self.execute(query)
                query1 = db.select([Customer])
                results = self.fetchall(query1)
                print(results)
                print(ResultProxy)
                print('Account closed successfully!\n\n')
            
            else:
                logger.error("ValueError. Invalid input for the account number: '{}' in close(). Account is already closed".format(self.acc_no))
                print("\n*******\nInvalid input!\n*********\n ValueError. The account is already closed. Please try again!\n")
                self.main()
            
        except TypeError:
            
            logger.error("TypeError. Invalid input for the account number: '{}' in close().".format(self.acc_no))
            print("\n*******\nInvalid input!\n*********\n TypeError. Please try again!\n")
            
            
        

    def closeall(self):
        print('\n  Thank you for using the Bank')
        sys.exit(0)

    def check_status(self, acc_no):

        try:

            query = db.select([Customer.columns.status]).where(
                Customer.columns.acc_no == acc_no)

            p = self.fetchone(query)
            print('\n  The account is {}'.format(p[0]))
            return p

        except TypeError as err:
            print(
                "\n********\nInvalid input!\n*********\n TypeError. Please try again!\n")

            logger.error(
                "Type Error. Invalid input: with the account number:'{}'.in check_status()".format(acc_no))

    def main(self):

        while True:

            print("\n----- MAIN MENU ----- ")
            print("\n1.  Create Account")
            print("\n2.  Deposit")
            print('\n3.  Withdrawl')
            print('\n4.  Check account status')
            print('\n5.  Close account')
            print('\n6.  Close application')
            print('\n\n')

            option = input('Enter your option: ')
            if option == '1':
                self.create_acc()
            elif option == '2':
                self.deposit()
            elif option == '3':
                self.withdraw()
            elif option == '4':
                n = input('Enter the account number: ')
                o = self.check_status(n)
            elif option == '5':
                self.close()
            elif option == '6':
                self.closeall()
            else:
                logger.error( "Type Error. Invalid input in main()")
                print('\nWrong option, try again')


if __name__ == '__main__':

    run_application = Bank()
