from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Встановлення відношення "один до багатьох" з таблицею Employee
    employees = relationship("Employee", back_populates="department")
