#crud.py的改写版本
from sqlalchemy import create_engine
from consts import DB_URI

eng = create_engine(DB_URI)
with eng.connect() as con:
    con.execute('drop table if exists users')
    con.execute('create table users(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))')
    con.execute("insert into users(Name) values('xiaoming')")
    con.execute("insert into users(Name) values('wanglang')")
    rs = con.execute('select * from users')
    for row in rs:
        print row

        