import sqlalchemy as sqlA
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect, select, func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship("Address", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(20), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")
    
    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"
    
print(User.__tablename__)
print(Address.__tablename__)

# conexão com banco de dados
engine = create_engine("sqlite://")

# criando as classes como tabela no banco de dados
Base.metadata.create_all(engine)

# depreciado = sera removido em futuro release
# print(engine.table_names())

# investiga o esquema do banco de dados
inspetor_engine = inspect(engine)

print(inspetor_engine.has_table("user_account"))

print(inspetor_engine.get_table_names())

print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    ariel = User(
        name='ariel',
        fullname='Ariel Riello',
        address=[Address(email_address='ariel@email.com')]
    )

    mirella = User(
        name='mirella',
        fullname='Mirella Ferreira',
        address=[Address(email_address='miferreira@email.com'),
                Address(email_address='mirella@email.org')]
    )

    random = User(name='random', fullname='Exemplo')

    # enviando para o banco de dados - BD (persistencia de dados)
    session.add_all([ariel, mirella, random])

    session.commit()

stmt = select(User).where(User.name.in_(['ariel', 'mirella']))
print('Recuperando usuarios a partir de uma condicao de fitragem')
for user in session.scalars(stmt):
    print(user)

stm_address = select(Address).where(Address.user_id.in_([2]))
print('Recuperando os enderecos de e-mail de Mirella')
for address in session.scalars(stm_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())
print('\nRecuperando info de maneira ordenada')
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print('\nExecutando statement a partir da connection')
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(User)
print('\nTotal de instancias em User')
for result in session.scalars(stmt_count):
    print(result)