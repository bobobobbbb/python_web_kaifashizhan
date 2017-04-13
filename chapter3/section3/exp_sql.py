from sqlalchemy import create_engine, Table, MetaDate, 
users = Table("Users", meta, Column('Id', Integer, primary_key=True, autoincrement=True)