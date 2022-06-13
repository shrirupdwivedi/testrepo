#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:06:42 2022

@author: shrirupdwivedi
"""
import mysql.connector
class SqlFuncs:
    """
    class SqlFuncs is created to access the essential mysql.connector's functions
    """

    def __init__(self):
        self._conn = mysql.connector.connect(host="localhost", user="root", password="12345678")  # use your password here
        self._cursor = self._conn.cursor()
        #self.cursor.execute("CREATE DATABASE mydatabase")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def execute(self, sql, params=None):
        """Implements execute function"""
        self.cursor.execute(sql, params or ())

    def commit(self):
        """Implements commit function"""
        self.connection.commit()

    def fetchall(self):
        """Implements fetchall function"""
        return self.cursor.fetchall()

    def fetchone(self):
        """Implement fetchone function"""
        return self.cursor.fetchone()

    def close(self, commit=True):
        """Implement close function"""
        if commit:
            self.commit()
        self.connection.close()



class Bank(SqlFuncs):
    """
   UnknownBank is a basic Banking system application that consists of some essential banking transactions
   1. Create Banking Account
   2. Deposit Amount
   3. Withdraw Amount
   4. Close Account
   5. Account Details (Customer information, Balance and Account type)
   """
    
    def __init__(self):
        SqlFuncs.__init__(self)
        self.create()
        
    def dash(self):
        
        option=int(input('Input your options'))
        
        if option == 1:
            self.create()
        elif option == 2:
            self.deposit()
        elif option == 3:
            self.withdraw()
        elif option == 4:
            self.close()
        elif option == 5:
            self.details()
            
    def create(self):
        
        self.first_name = input('Enter your first name: ')
        self.last_name = input('Enter your last name: ')
        self.phone_no = input('Enter your phone number: ')
        self.dob = input('Enter your date of birth: ')
        self.email = input('Enter your email ID: ')
        self.acctype = input('Enter your account type: ')
        self.balance = input('Enter the opening balance: ')
        
        #cmd = "INSERT INTO customer(first_name,last_name,phone_no,dob,email,acctype,balance,accstatus) \
           # VALUES (%s, %s, %s, %s, %s, %s, %s, 'Active');
           # cctype))
    
        cmd = "NSERT INTO customer(first_name,last_name,phone_no,dob,email,acctype,accstatus) \
            VALUES (%s, %s, %s, %s, %s, %s, 'Active');"

        self.execute(cmd,(self.first_name, 
                           self.last_name, 
                           self.dob, 
                           self.phone_no, 
                           self.email, 
                           self.acctype, 
                           self.balance))

    def deposit(self):
        
        self.accno = input('Enter account number')
        self.amount = input('Enter the amount to deposit')
        self.balance+= self.amount
        
    
    def acc_status(self,acc_num):
        
        cmd = "SELECT status FROM customer WHERE acc"
        
        
    
    
        
            
            
            
        
        