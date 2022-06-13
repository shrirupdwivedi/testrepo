import sqlalchemy as db



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

# query = db.insert(Customer).values(first_name='naveen', last_name='dwivedi', status='Active') 
# #ResultProxy = connection.execute(query)

# results = connection.execute(db.select([Customer])).fetchall()
# print(results)

class sql():
    
    def execute(self,query):
        return connection.execute(query)
        
    def fetchall(self,query):
        return connection.execute(query).fetchall()

        
        
            
class bank(sql):
    
    def __init__(self):
        
    
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
bank()
