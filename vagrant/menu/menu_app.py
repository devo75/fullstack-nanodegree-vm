from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

restaurant1 = Restaurant(name = "Pizza Palace")
session.add(restaurant1)
session.commit()

cheesepizza = MenuItem(name = "Cheese Pizza",
                      description = "made with all natural ingredients and fresh cheese",
                      course = "Entree",
                      price = "8.99",
                      restaurant = restaurant1)
session.add(cheesepizza)
session.commit()

restaurant2 = Restaurant(name= "Veggie Delight")
session.add(restaurant2)
session.commit()




            
