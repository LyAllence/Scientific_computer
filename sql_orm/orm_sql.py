#!/usr/bin/env python3
# coding: utf-8

import configparser
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy import and_, or_
from sqlalchemy.sql import func


Base = declarative_base()
session = None 


class Orm_Mysql(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'one'):
            cls.one = super(Orm_Mysql, cls).__new__(cls)
        return cls.one

    def __init__(self, sql_url):
        self.engine = create_engine(sql_url)


# class user
class Users(Base):

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    extra = Column(String(16))

    __table_args__ = (
                       UniqueConstraint('id', 'name', name='uix_id_name'),
                       Index('ix_id_name', 'name', 'extra'),
                     )


# test
class Test(Base):
    __tablename__ = 'test'
    name = Column(String(10), primary_key=True)


# class favor
class Favor(Base):

    __tablename__ = 'favor'
    nid = Column(Integer, primary_key=True)
    caption = Column(String(50), default='red', unique=True)


# class person
class Person(Base):
    
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    favor_id = Column(Integer, ForeignKey("favor.nid"))


# class group
class ServerToGroup(Base):
    __tablename__ = 'servertogroup'
    nid = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))


# class group
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)


# class server
class Server(Base):
    __tablename__ = 'server'

    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    port = Column(Integer, default=22)


# some oprate
def oprate_orm():
    # add
    obj = Users(name="alex0", extra='sub')
    session.add(obj)
    session.add_all([
        Users(name="alex1", extra='sub'),
        Users(name="alex2", extra='sub'),
        Users(name="alex3", extra='sub')
    ])
    session.commit()

    print('ADD:', session.query(Users).all())
    
    # minus
    session.query(Users).filter(Users.id > 2).delete()
    session.commit()
    
    print('MINUS', session.query(Users).all())
    
    # update
    session.query(Users).filter(Users.id > 2).update({"name" : "099"})
    session.query(Users).filter(Users.id > 2).update({Users.name: Users.name + "099"}, synchronize_session=False)
    session.query(Users).filter(Users.id > 2).update({"name": Users.name + '1'}, synchronize_session="fetch")
    session.commit()

    print('UPDATE', session.query(Users).all())

    # select
    ret = session.query(Users.name, Users.extra).all()
    ret = session.query(Users).filter_by(name='alex').all()
    ret = session.query(Users).filter_by(name='alex').first()


def other_oprate():
    ret = session.query(Users).filter_by(name='alex').all()
    ret = session.query(Users).filter(Users.id > 1, Users.name == 'eric').all()
    ret = session.query(Users).filter(Users.id.between(1, 3), Users.name == 'eric').all()
    ret = session.query(Users).filter(Users.id.in_([1,3,4])).all()
    ret = session.query(Users).filter(~Users.id.in_([1,3,4])).all()
    ret = session.query(Users).filter(Users.id.in_(session.query(Users.id).filter_by(name='eric'))).all()
    ret = session.query(Users).filter(and_(Users.id > 3, Users.name == 'eric')).all()
    ret = session.query(Users).filter(or_(Users.id < 2, Users.name == 'eric')).all()
    ret = session.query(Users).filter(
        or_(
            Users.id < 2,
            and_(Users.name == 'eric', Users.id > 3),
            Users.extra != ""
        )).all()
    print('and_ and or_:', ret)

    ret = session.query(Users).filter(Users.name.like('e%')).all()
    print('%:', ret)

    ret = session.query(Users).order_by(Users.name.desc(), Users.id.asc()).all()
    print('order:', ret)

    ret = session.query(
        func.max(Users.id),
        func.sum(Users.id),
        func.min(Users.id)).group_by(Users.name).having(func.min(Users.id) >2).all()
    print('group:', ret)

    ret = session.query(Person).join(Favor, isouter=True).all()
    print('join:', ret)

    q1 = session.query(Users.name).filter(Users.id > 2)
    q2 = session.query(Favor.caption).filter(Favor.nid < 2)
    ret = q1.union_all(q2).all()
    print('union:' , ret)


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('./config.ini')
    mysql_url = config.get('pymysql', 'sql')
    orm = Orm_Mysql(mysql_url)
    # create table
    # Base.metadata.create_all(orm.engine)
    
    Session = sessionmaker(bind=orm.engine)
    session = Session()
    # Base.metadata.create_all(orm.engine)
    # oprate_orm()
    # other_oprate()
