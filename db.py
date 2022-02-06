from sqlalchemy import create_engine, Column, String, Text, Integer, LargeBinary

#from imagetostring import readbyte

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///backend.db', echo=False, connect_args={'check_same_thread': False})

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Product(Base):
	__tablename__ = 'Product'
	
	id = Column(Integer, primary_key= True)
	name = Column(Text(50))
	price = Column(Integer)
	description = Column(Text())
	image = Column(Text())
	
Base.metadata.create_all(engine)

#newStuff = Product(name='Car', price=120, description='Fast, fast, fast', image="/assets/ezugwu.jpg")
#session.add(newStuff)
#session.commit()