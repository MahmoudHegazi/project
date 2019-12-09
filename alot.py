from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Car, Base, CarType, User

engine = create_engine('sqlite:///cars.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for Ferrari
car1 = Car(user_id=1, name="Ferrari")

session.add(car1)
session.commit()

cartype1 = CarType(user_id=1, name="488 Pista", description="Model Year: 2020,State: New ,color: gold, CC: 6500, only 1 piece available, for offer call : 01113722390",
                     price="$3.350.000.00" , car=car1)

session.add(cartype1)
session.commit()


cartype2 = CarType(user_id=1, name="GTC4Lusso", description="Model Year: 2020,State: New ,color: black, CC: 2000, available",
                     price="$500.120.00", car=car1)

session.add(cartype2)
session.commit()

cartype3 = CarType(user_id=1, name="Portofino", description="Model Year: 2019,State: New ,color: white, CC: 2000, available after 1 week",
                     price="$500.500.00", car=car1)

session.add(cartype3)
session.commit()

cartype4 = CarType(user_id=1, name="A2", description="Model Year: 2020,State: New ,color: black, CC: 2500, available",
                     price="$300.000.00", car=car1)

session.add(cartype4)
session.commit()

cartype5 = CarType(user_id=1, name="mini van", description="Model Year: 2020,State: New ,color: black, CC: 2600, available",
                     price="$700.000.99", car=car1)

session.add(cartype5)
session.commit()

cartype6 = CarType(user_id=1, name="Super Fast", description="Model Year: 2020,State: New ,color: green, CC: 2500, available",
                     price="$105.000.99",  car=car1)

session.add(cartype6)
session.commit()

cartype7 = CarType(user_id=1, name="GTC6Lusso", description="Model Year: 2020,State: New ,color: orange, CC: 1500, available",
                     price="$200.000.99", car=car1)

session.add(cartype7)
session.commit()

cartype8 = CarType(user_id=1, name="GTC2Lusso",
                     description="Model Year: 2016,State: New ,color: black, CC: 2500, available", price="$300.000.49", car=car1)

session.add(cartype8)
session.commit()

cartype9 = CarType(user_id=1, name="499 Pista", description="Model Year: 2020,State: New ,color: black, CC: 1500, available",
                     price="$155.000.99", car=car1)

session.add(cartype9)
session.commit()


# Menu for Audi
car1 = Car(user_id=1, name="Audi")

session.add(car1)
session.commit()


cartyp1 = CarType(user_id=1, name="RS5 Sportback", description="Model Year: 2020,State: New ,color: black, CC: 2500, available",
                     price="$700.000.99", car=car1)

session.add(cartyp1)
session.commit()

cartyp2 = CarType(user_id=1, name="Audi Q3",
                     description="Model Year: 2020,State: New ,color: black, CC: 2000, available", price="$250.000.00", car=car1)

session.add(cartyp2)
session.commit()

cartyp3 = CarType(user_id=1, name="Audi R8", description="Model Year: 2019,State: New ,color: white, CC: 2000, available after 1 week",
                     price="$150.000.00", car=car1)

session.add(cartyp3)
session.commit()



# Menu for Ford
car1 = Car(user_id=1, name="Ford")

session.add(car1)
session.commit()


cartyp1 = CarType(user_id=1, name="Ford Mustang", description="Model Year: 2020,State: New ,color: green, CC: 2000 available",
                     price="$208.000.99", car=car1)

session.add(cartyp1)
session.commit()

cartyp2 = CarType(user_id=1, name="Chinese Dumplings", description="Model Year: 2020,State: New ,color: blue, CC: 1600, available",
                     price="$600.000.99", car=car1)

session.add(cartyp2)
session.commit()

cartyp3 = CarType(user_id=1, name="Gyoza", description="Model Year: 2020,State: New ,color: orange, CC: 1300, available soon call us on 01113722390",
                     price="$190.000.95", car=car1)

session.add(cartyp3)
session.commit()




# Menu for Cadillac
car1 = Car(user_id=1, name="Cadillac")

session.add(car1)
session.commit()


cartyp1 = CarType(user_id=1, name="Cadillac CTS", description="Model Year: 2020,State: New ,color: white, CC: 2000, available.",
                     price="$200.000.99", car=car1)

session.add(cartyp1)
session.commit()

cartyp2 = CarType(user_id=1, name="Cadillac XT4", description="Model Year: 2017,State: used ,color: blue, CC: 1500, available",
                     price="$500.000.99", car=car1)

session.add(cartyp2)
session.commit()

cartyp3 = CarType(user_id=1, name="Cadillac XT5",
                     description="Model Year: 2020,State: New ,color: red, CC: 1800, available after 2 weeks ", price="$240.000.50", car=car1)

session.add(cartyp3)
session.commit()



# Menu for Mercedes
car1 = Car(user_id=1, name="Mercedes")

session.add(car1)
session.commit()


cartyp1 = CarType(user_id=1, name="Mercedes-Benz E-Class", description="Model Year: 2020,State: New ,color: red, CC: 2800",
                     price="$130.000.95", car=car1)

session.add(cartyp1)
session.commit()

cartyp2 = CarType(user_id=1, name="Mercedes-Benz C-Class", description="Model Year: 2020,State: New ,color: red, CC: 2000",
                     price="$400.000.95", car=car1)

session.add(cartyp2)
session.commit()

cartyp3 = CarType(user_id=1, name="Mercedes-Benz GLA", description="Model Year: 2020,State: used ,color: red, CC: 2000",
                     price="$600.000.95", car=car1)

session.add(cartyp3)
session.commit()

cartyp4 = CarType(user_id=1, name="Mercedes-Benz CLA",
                     description="Model Year: 2020,State: used ,color: red, CC: 2000", price="$300.500.95", car=car1)

session.add(cartyp4)
session.commit()



# Menu for Toyota
car1 = Car(user_id=1, name="Toyota")

session.add(car1)
session.commit()


cartyp1 = CarType(user_id=1, name="corolla", description="Model Year: 2020, State: New ,color: white, CC: 2600",
                     price="$190.000.95", car=car1)

session.add(cartyp1)
session.commit()

cartyp2 = CarType(user_id=1, name="yaris", description="Model Year: 2005, State: Used ,color: black, CC: 1300",
                     price="$170.000.95", car=car1)

session.add(cartyp2)
session.commit()

cartyp3 = CarType(user_id=1, name="Jeb", description="Model Year: 2020, State: New ,color: blue, CC: 1600",
                     price="$650.000.50", car=car1)

session.add(cartyp3)
session.commit()

cartyp4 = CarType(user_id=1, name="super Crolla", description="Model Year: 2005, State: Used ,color: white, CC: 1300",
                     price="$160.000.75", car=car1)

session.add(cartyp4)
session.commit()

cartyp5 = CarType(user_id=1, name="Crolla Beginto", description="Model Year: 2020, State: New ,color: black, CC: 1600",
                     price="$700.000.00", car=car1)

session.add(cartyp5)
session.commit()


# Menu for BMW
car1 = Car(user_id=1, name="BMW")

session.add(car1)
session.commit()

cartyp1 = CarType(user_id=1, name="Class A",
                     description="Model Year: 2020, State: New ,color: black, CC: 1600", price="$280.000.99", car=car1)

session.add(cartyp1)
session.commit()


cartyp2 = CarType(user_id=1, name="BMW Class C", description="Model Year: 2018, State: New ,color: black, CC: 2000",
                     price="$200.000.99", car=car1)

session.add(cartyp2)
session.commit()

cartyp3 = CarType(user_id=1, name="classic BM", description="Model Year: 2005, State: Used ,color: black, CC: 1800",
                     price="$100.000.95", car=car1)

session.add(cartyp3)
session.commit()

cartyp4 = CarType(user_id=1, name="BMW A0",
                     description="Model Year: 2020, State: New ,color: green, CC: 2600", price="$170.000.50", car=car1)

session.add(cartyp4)
session.commit()

cartyp5 = CarType(user_id=1, name="BMW Beganto", description="Model Year: 2020,State: New ,color: red, CC: 1800, available after 2 weeks.",
                     price="$280.000.95", car=car1)

session.add(cartyp5)
session.commit()

cartyp6 = CarType(user_id=1, name="BMW ghost", description="Model Year: 2017,State: used ,color: blue, CC: 1500, available",
                     price="$129.000.50", car=car1)

session.add(cartyp6)
session.commit()

cartyp7 = CarType(user_id=1, name="Mini BMW", description="Model Year: 2020,State: New ,color: white, CC: 2000, available",
                      price="$100.000.99", car=car1)

session.add(cartyp7)
session.commit()





print "added menu items!"
