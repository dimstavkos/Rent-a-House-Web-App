from sqlalchemy.orm import Session

from controllers.PropertyController import PropertyController
from database.database import SessionLocal
from models.Role import Role
from models.Location import Location
from faker import Faker
from models.Property import Property
from models.Review import Review
from models.IndoorSpace import IndoorSpace
from models.PropertyRuleList import PropertyRuleList
from models.UserHasReview import UserHasReview
from models.UserMessage import UserMessage
from models.Photo import Photo
from models.Booking import Booking
from models.AvailableDate import AvailableDate
from models.User import User
from models.PropertyType import PropertyType
from passlib.context import CryptContext

from controllers.ExportController import ExportController

if __name__ == "__main__":
    db = SessionLocal()
    controller = PropertyController()

    results = controller.recommend(db, 5)

    i = 0
    for x in results:
        print(x.id, end="")
        print('\t', end="")
        i=i+1
        if i %10 == 0:
            print('')

