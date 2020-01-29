import sqlite3

conn = sqlite3.connect('test.db')

#conn.execute('create table emp1(id number(5),name varchar2(50),salary number(8,2));')
#conn.ex
n = int(input("Enter num of records you want to insert : - "))
st = ""
for i in range(1,n+1):
    no = input("Enter emp id : - ")
    name = input("Enter emp name : - ")
    sal = input("Enter emp salary : - ")

    st = "INSERT INTO emp1 (id,name,salary) VALUES ("+no+",'"+name+"',"+sal+")"
    conn.execute(st)
    conn.commit()

cur = conn.execute('select * from emp1')
for j in cur:
    print(j)
conn.commit()
conn.close()