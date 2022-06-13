#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:11:43 2022

@author: shrirupdwivedi
"""
class SqlFuncs:
    """
    class SqlFuncs is created to access the essential mysql.connector's functions
    """

    def __init__(self):
        self._conn = mysql.connector.connect(**config)  # use your password here
        self._cursor = self._conn.cursor()

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