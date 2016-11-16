'''
create records in db
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Shelter, Base, Puppy

# create engine, let program know which db engine we want to use
engine = create_engine('sqlite:///shelterpuppy.db')

# bind the engine with base class
Base.metadata.bind = engine

# create connection between engine and code execution
DBSession = sessionmaker(bind = engine)

# create sessions for db work
session = DBSession()

# create my first restaurant called 'Pizza Palace'
myFirstRestaurant = Restaurant(name = 'Pizza Palace')
session.add(myFirstRestaurant)
session.commit()
cheesePizza = MenuItem(name        = 'Cheese Pizza'
                      ,description = 'Made with all natural ingredients'
                      ,course      = 'Entree'
                      ,price       = '$8.99'
                      ,restaurant  = myFirstRestaurant
                      )
session.add(cheesePizza)
session.commit()

# query the db to make sure everything created as expected
menuItems = session.query(MenuItem).all()
for menuItem in menuItems:
    print menuItem.price
