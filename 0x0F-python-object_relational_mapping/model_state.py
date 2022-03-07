#!/usr/bin/python3
"""
python script that contains the class definition of a State and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


class state(Base):
    """class state for the state table
    """

    __tablename__ = "states"
    id = column(
            integer,
            autoincrement=True,
            unique=True,
            nullable=False,
            primary_key=True
            )
    name = column(
            string(length=128),
            nullable=False
            )
