from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()

cheesepizza = MenuItem(name="Cheese Pizza", 
                       description = "Made with all natural ingredients and fresh mozzarella", 
                       course="Entree", 
                       price="$8.99", 
                       restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()

#firstResult = session.query(Restaurant).first()
#firstResult.name

restaurants = session.query(Restaurant).all()
for restaurant in restaurants:
    print(restaurant.name)

items = session.query(MenuItem).all()
for item in items:
    print(item.name + " " + item.price)

