from models import Dog
from models import Dog

# This python FN, create_table, is used to create a dB table using SQLAlc. 
# In summary, this FN is a part of the setup process for a SQLAlc. app, where it creates all the necessary tables in the DB.
def create_table(base, engine):
    base.metadata.create_all(engine)


# This python FN, save, is used to persist an instance of a dog obj. to a DB using SQLAlc. 
# In summary, this FN is used to save a dog obj. to the DB using SQLAlc. It's a common pattern in apps that use SQLAlc to interact with DB's.
def save(session, dog):
    session.add(dog)
    session.commit()



# This Py. FN, get_all, is used to retrieve all instances of the Dog class from a DB using SQLAlc. 
# In summary, this FN is used to retrieve all Dog obj's from the DB using SQLAlc. It's a common pattern in apps that use SQLAlc to interact with DB's.
def get_all(session):
    return session.query(Dog).all()


# This Python FN, find_by_name, is used to retrieve the first instance of the Dog class from a DB that matches a specified name.
# This FN is used to retrieve the first Dog obj. from the DB that matches a specified name
def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()


# This Py. FN, find_by_id, is used to retrieve the first instance of the Dog class from a database that matches a specified id. 
def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()


# This Py. FN, find_by_name_and_breed, is used to retrieve the first instance of the Dog class from a DB that matches a specified name & breed. 
def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

# This Py. FN, update_breed, is used to update the breed of a specific Dog instance in the DB.
def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()

