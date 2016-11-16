from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from puppies import Base, Shelter, Puppy
import datetime
# pre db setup
engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


'''
Q1: query all of the puppies and return the results in ascending alphabetical order
'''
def query1():
    result = session.query(Puppy.name).order_by(Puppy.name.asc()).all()
    for item in result:
        print item[0]

'''
Q2: query all the puppies that are less than 6 months old organized by the youngest first
'''
def query2():
    date = datetime.date.today()
    if passesLeapDay(date):
        sixMonth = date - datetime.timedelta(days = 183)
    else:
        sixMonth = date - datetime.timedelta(days = 182)
        result = session.query(Puppy.name,Puppy.dateOfBirth). \
                 filter(Puppy.dateOfBirth >= sixMonth) \
                 .order_by(Puppy.dateOfBirth.desc())
        for item in result:
            print '{name}:, {dob}'.format(name = item[0], dob = item[1])

def query3():
    result = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight.asc()).all()
    for item in result:
        print item[0], item[1]

def query4():
    result = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Puppy.shelter_id).all()
    for item in result:
        print item[0].id, item[0].name, item[1]

def passesLeapDay(date):
    thisYear = date.timetuple()[0]
    if isLeapYear(thisYear):
        sixMonth = date - datetime.timedelta(days = 183)
        leapDay = datetime.date(thisYear, 2, 29)
        return leapDay >= sixMonth
    else:
        return False
def isLeapYear(thisYear):
    if thisYear % 4 != 0:
        return False
    elif thisYear % 100 != 0:
        return True
    elif thisYear % 400 != 0:
        return False
    else:
        return True
#query1()
#query2()
#query3()
query4()
