# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:28:47 2020

@author: USER
"""
'''
암호화기능
'''

import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

# db를 저장하려면 무조건 확장자는 .db
con = sqlite3.connect("c:/spyder_python/2020-04-21/kospi.db")
print(type(con))

cursor = con.cursor()

# cursor.execute("CREATE TABLE kakao(Date text, Open int, High int, Low int, Closing int, Volumn int)")

cursor.execute("INSERT INTO kakao VALUES('16.06.03', 97000, 98600, 96900, 98000, 321405)")

cursor.execute("SELECT * FROM kakao")
print(cursor.fetchone())
print(cursor.fetchone())

con.commit()
# con.close()

cursor.execute("SELECT * FROM kakao")
kakao = cursor.fetchall()
print(type(kakao))
print(kakao[0][0])
print(kakao[0][1])
print(kakao[0][2])
print(kakao[0][3])

con.commit()
con.close()
