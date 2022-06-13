#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:56:29 2022

@author: shrirupdwivedi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 12:13:01 2022

@author: shrirupdwivedi
"""

import sqlalchemy as db
import sys


#!/usr/bin/env python3
# -*- coding: utf-8 -*-



 

engine = db.create_engine('sqlite:///test.sqlite') #Create test.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()

Customer = db.Table('Customer', metadata,
              db.Column('acc_no',db.Integer(),primary_key=True,nullable=False,autoincrement=True),
              db.Column('first_name', db.String(255), nullable=False),
              db.Column('last_name', db.String(255)),
              db.Column('dob', db.Integer()),
              db.Column('email', db.String(255)),
              db.Column('acc_type', db.String(255)),
              db.Column('status', db.String(255)),
              db.Column('balance', db.Integer())
              
              )

metadata.create_all(engine) #Creates the table

print(engine.table_names())

class sql():
    
    def execute(self,query):
        return connection.execute(query)
    
    def fetchall(query):
        return connection.execute(query).fetchall()
    

class bank():
    
    def __init__(self):
        
        self.main()
    
    def create_acc(self):
        
        self.first_name = input("Enter the account holder first name : ")
        self.last_name = input("Enter the account holder last name : ")
        self.dob = input("Enter the account holder date of birth : ")
        self.email = input("Enter the account holder email: ")
        self.acc_type = input("Account type (saving/checking): ")
        self.balance = input("Enter opening balance: ")
        
        query = db.insert(Customer).values(first_name=self.first_name, last_name=self.last_name,dob=self.dob,\
                                            status='Active',email=self.email,acc_type=self.acc_type,\
                                                balance=self.balance)
    
        ResultProxy = connection.execute(query)
        results = connection.execute(db.select([Customer])).fetchall()
        print(results)
        
        print('New customer added successfully!\n\n')
    
    def deposit(self):
        
    
        self.acc_no=input('Enter your account number: ')
        self.balance=input('Enter the amount to deposit: ')
        self.balance=int(self.balance)
    
        
        query = Customer.update().values(balance=self.balance+Customer.columns.balance)\
            .where(db.and_(Customer.columns.acc_no == self.acc_no, Customer.columns.status == 'Active'))
     
         
        ResultProxy = connection.execute(query)
        results = connection.execute(db.select([Customer])).fetchall()
        print(results)
        
        print('Deposited successfully!\n\n')
        
    def withdraw(self):
        
        self.acc_no=input('Enter your account number: ')
        self.balance=input('Enter the amount to withdraw: ')
        self.balance=int(self.balance)
    
        
        query = Customer.update().values(balance=self.balance-Customer.columns.balance)\
            .where(db.and_(Customer.columns.acc_no == self.acc_no,Customer.columns.status == 'Active'))
     
         
        ResultProxy = connection.execute(query)
        results = connection.execute(db.select([Customer])).fetchall()
        print(results)
        
        print('Withdrawl conducted successfully!\n\n')
        
            
    def close(self):
        
        self.acc_no = input('Enter the account number of the account to be closed: ')
        
        query = Customer.update().values(status='Inactive')\
            .where(db.and_(Customer.columns.acc_no == self.acc_no,Customer.columns.status == 'Active') )
     
         
        ResultProxy = connection.execute(query)
        results = connection.execute(db.select([Customer])).fetchall()
        print(results)
        print('Account closed successfully!\n\n')
    
    def closeall(self):
        print('Thank you for using the Bank')
        sys.exit(0)
        
    def check_status(self):
        
        
        
    def main(self):
    
        
        while True:
            
            print("\n----- MAIN MENU ----- ")
            print("\n1.  Create Account")
            print("\n2.  Deposit")
            print('\n3.  Withdrawl')
            print('\n4.  Close Account')
            print('\n5.  Close application')
            print('\n\n')
        
            option = input('Enter your option: ')
            if option == '1':
                self.create_acc()
            elif option == '2':
                self.deposit()
            elif option == '3':
                self.withdraw()
            elif option == '4':
                self.close()
            elif option == '5':
                self.closeall()

            
        
bank()            
