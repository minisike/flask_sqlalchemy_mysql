from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey

engine = create_engine("mysql+pymysql://root:wwwwwwww@127.0.0.1:3306/web_flask", echo=True)

metadata = MetaData(engine)

user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(20)),
    Column('fullname', String(40)),
    )
address_table = Table('address', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', None, ForeignKey('user.id')),
    Column('email', String(128), nullable=False)
    )

metadata.create_all()