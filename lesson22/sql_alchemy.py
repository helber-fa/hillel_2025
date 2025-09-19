import time

from sqlalchemy import create_engine, Column, Integer, String, func, ColumnOperators, select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from core.db.orm_lesson.tables.user import User
from faker import Faker

# З'єднання з базою даних PostgreSQL (замініть дані на ваші)
PG_SQL = "postgresql://postgres:2410ghjnjy@localhost:5432/hillel_2025"
SQLITE_SQL = rf""
engine = create_engine(PG_SQL)
local_faker = Faker()
# Створення базового класу для визначення моделей даних
Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users_orm'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String, unique=True)
#     age = Column(Integer)

# Створення таблиці у базі даних
# Base.metadata.create_all(engine)

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

# for _ in range(5):
#     session.add(User(name=f"test-{local_faker.name()}-{time.time()}", age=25)) #INSERT INTO/додавання користувачів
# all_users = session.query(User).all()
# # print(all_users, sep="\n")
# print(*all_users, sep="\n")
# all_users_number = session.query(User).count()
# print("Count all users", all_users_number)
# first_user = session.query(User).first()
# print("First user:",first_user)
# particular_user = session.query(User).get(9)
# print("User with id 9:",particular_user)

# user_bob = session.query(User).where(User.name == "Bob").first()
user_bob = session.execute(select(User).where(User.name == "Bob")).first()
print(user_bob[0])
session.commit()
session.close()
# session.add_all([
#     User(name='John', age=30),
#     User(name='Alice', age=25),
#     User(name='Bob', age=35),
# ]) # так як імена унікальні - код спрацює лише раз

# транзакції

try:
    session.begin()
    all_users = session.query(User).all()
    all_users[1].name = "Custom user"
    session.commit()
    raise AttributeError("Some custom error")
except:
    print("Something went wrong")
    session.rollback()
finally:
    session.commit()








