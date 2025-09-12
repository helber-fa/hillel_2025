from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))

    # Встановлення відношення "багато до одного" з таблицею Department
    department = relationship("Department", back_populates="employees")
