import sqlite3

conn = sqlite3.connect('test.db')

#conn.execute('create table emp1(id number(5),name varchar2(50),salary number(8,2));')
#conn.ex
# print('Enter 1 for insert data in table')
# print('Enter 2 for display data')
# print('Enter 3 for update data')
# print('Enter 4 for delete selected data')
# print('Enter 5 for drop the table')
# print('Enter q for quit')
# ch = int(input('Enter the choice : - '))

flag = True

while flag:
    print('Enter 1 for insert data in table')
    print('Enter 2 for display data')
    print('Enter 3 for update data')
    print('Enter 4 for delete selected data')
    print('Enter 5 for drop the table')
    print('Enter q for quit')
    ch = input('Enter the choice : - ')

    if ch == '1':
        n = int(input("Enter num of records you want to insert : - "))
        st = ""
        for i in range(1,n+1):
            no = input("Enter emp id : - ")
            name = input("Enter emp name : - ")
            sal = input("Enter emp salary : - ")

            st = "INSERT INTO emp1 (id,name,salary) VALUES ("+no+",'"+name+"',"+sal+")"
            conn.execute(st)
            #conn.commit()

    elif ch == '2':
        print('\tEnter 1 for show all data of table')
        print('\tEnter 2 for show selected data from table')

        sel = input('Enter choice for displaying data : - ')
        if sel == '1':
            cur = conn.execute('select * from emp1')
            for j in cur:
                print('Emp id : - ',j[0])
                print('Emp name : - ', j[1])
                print('Emp salary : - ', j[2])

        elif sel == '2':
            sid = input('Enter id : - ')
            cur = conn.execute('select * from emp1 where id='+sid)
            for j in cur:
                print('Emp id : - ', j[0])
                print('Emp name : - ', j[1])
                print('Emp salary : - ', j[2])

    elif ch == '3':
        uid = input('Enter id you want to update : - ')
        usal = input('Enter updated salary : - ')
        conn.execute("UPDATE emp1 set SALARY = "+usal+" where ID = "+uid)

    elif ch == '4':
        uid = input("Enter id to delete record : - ")
        conn.execute('delete from emp1 where id = '+uid)

    elif ch == '5':
        conn.execute('drop table emp1')

    elif ch == 'q':
        flag = False

    # ch = int(input('Enter the choice : - '))

    conn.commit()
conn.close()