from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()

# DEFINE THE ENGINE (CONNECTION OBJECT)

# IT'S FOR DEFAULT DATABASE SQLITE

# sqlalchemy2.0

#engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
#engine = db.create_engine('sqlite:///footprint.db', echo=True)

# FOR MYSQL USER
engine = db.create_engine('mysql://scott:tiger@localhost/mydatabase')

#   'mysql+pymysql://root:pass@localhost/footprint')


class Profile(Base):
    __table_name__ = 'profile'
    email = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100))
    contact = db.Column(db.Integer)

class Location(Base):
    __table_name__ = 'location'
    email = db.Column(db.String(50), primary_key=True)
    location = db.Column(db.String(100))


# Create session object 
Session = sessionmaker(bind=engine)
session = Session()

# SELECT * FROM Profile
result = session.query(
    Profile.email,
    Profile.name, 
    Profile.contact,
    Location.location
    ).join(Location, Profile.email == Location.email)

print('Query:',result)

# VIEW THE ENTRIES IN THE RESULT
for r in result:
    print(r.email, "|", r.name, "|", r.contact, "|", r.location)
