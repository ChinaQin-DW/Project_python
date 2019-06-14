# coding: utf-8
# from sqlalchemy import Column, DECIMAL, String
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
# metadata = Base.metadata
from flask.ext.sqlalchemy import SQLAlchemy
from config import db
class TableShouye(db.Model):
    __tablename__ = 'table_shouye'
    xiaobiaoti = db.Column(db.String(50))
    neirong = db.Column(db.String(1000))
    xh = db.Column(db.DECIMAL(2, 0), primary_key=True)
