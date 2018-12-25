sqlalchemy:

1, can use sql grammer.

  db_engine = sqlalchemy.create_engine('xxx')

  db_conn = db_engine.connect()

  db_conn.execute(sql)

2, use object.

  2.1: create orm class:

    class Role(Base): # __table__ or __tablename__ must have, and primary_key is must have

      __tablename__ = 'roles'

      id = db.Column(db.Integer, primary_key=True)

  2.2: create table:  Base.metadata.create_all(orm.engine)
       drop table: Base.metadata.drop_all(engine)

  2.3: oprate sql:
       Session_Class = sessionmaker(bind=engine) # create talk with sql(this is a Class, need instantiate.)
       session = Session_Class() # get talk with sql
       # insert
       session.add(Role(id))
       # find
       session.query(Role).all()
       # delete
       session.query(Role).filter.delete()
       # update
       session.query(Role).filter.update({x:x})
       # delete, insert, update, need run session.commit()
       
