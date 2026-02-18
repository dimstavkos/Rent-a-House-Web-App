from datetime import datetime, timedelta

from sqlalchemy.orm import Session

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

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

faker = Faker()



def seedFixedProperties(db: Session, rows: int = 10):
    print("Generating Fixed Properties...")




    property_type_ids = [propertytype.id for propertytype in db.query(PropertyType).all()]

    user_ids = [user.id for user in db.query(User).all()]

    for i in range(0, rows):
        # Indoorspace
        indoorspace = IndoorSpace(bed_num=faker.random_int(min=1, max=8), bath_num=faker.random_int(min=1, max=8),
                                  bedroom_num=faker.random_int(min=1, max=5), has_livingroom=faker.pybool(),
                                  total_space=faker.random_int(min=50, max=5000),
                                  description=faker.paragraph(nb_sentences=1),
                                  property_type_id=faker.random_element(elements=property_type_ids))
        db.add(indoorspace)
        db.commit()

        # Location

        countryList = ["Greece", "France"]
        cityList = ["Athens", "Paris"]
        addressList = ["Stadiou", "Rue Paris"]

        addressNum = faker.random_int(min=1,max=30)


        if i%2 == 0:
            country = countryList[0]
            city = cityList[0]
            address  = addressList[0]
        else:
            country = countryList[1]
            city = cityList[1]
            address = addressList[1]

        location = Location(country = country, city=city, address=address,latitude=23.2658, longitude=21.6548)
        db.add(location)
        db.commit()

        object = Property(price=faker.pydecimal(left_digits=3, right_digits=2, positive=True), has_wifi=faker.pybool(),
                          has_airconditioning=faker.pybool(), has_heat=faker.pybool(), has_kitchen=faker.pybool(),
                          has_tv=faker.pybool(), has_parking=faker.pybool(), has_elevator=faker.pybool(),
                          description=faker.paragraph(nb_sentences=3), floor=faker.random_int(min=1, max=10),
                          number_of_guests=faker.random_int(min=1, max=10), is_available=True,
                          user_id=faker.random_element(elements=user_ids), location_id=location.id,
                          indoor_space_id=indoorspace.id, property_created=faker.date(), property_updated=faker.date())
        db.add(object)
        db.commit()

        # Property rule list
        propertyRuleList = PropertyRuleList(smoking_allowed=faker.pybool(), pet_allowed=faker.pybool(),
                                            party_allowed=faker.pybool(),
                                            min_night_number=faker.random_int(min=1, max=20),
                                            property_id=object.id)
        db.add(propertyRuleList)
        db.commit()

        n = faker.random_int(1, 3)

        for j in range(n):
            photo_object = Photo(photo="https://picsum.photos/seed/" + faker.word() + "/410/225", property_id=object.id)
            db.add(photo_object)
            db.commit()

        n = faker.random_int(1, 15)

        for i in range(0, n):
            reviewObject = Review(rating=faker.random_int(min=1, max=5), comment=faker.paragraph(nb_sentences=3))
            db.add(reviewObject)
            db.commit()

            days = faker.random_int(3, 10)
            date_from = faker.date()
            start_date = datetime.strptime(date_from, "%Y-%m-%d")
            end_date = start_date + timedelta(days)
            date_to = end_date.strftime("%Y-%m-%d")

            bookingObject = Booking(start_date=date_from, end_date=date_to,
                                    total_night_num=days,
                                    total_price=faker.pydecimal(left_digits=3, right_digits=2, positive=True),
                                    user_id=faker.random_element(elements=user_ids),
                                    property_id=object.id,
                                    review_id=reviewObject.id, booking_created=faker.date(),
                                    booking_updated=faker.date(), booking_completed=faker.pybool(),
                                    booking_verified=faker.pybool())
            db.add(bookingObject)
            db.commit()

        n = faker.random_int(1, 5)

        for i in range(0, n):
            date_from = faker.date()
            start_date = datetime.strptime(date_from, "%Y-%m-%d")
            end_date = start_date + timedelta(days=faker.random_int(3, 10))
            date_to = end_date.strftime("%Y-%m-%d")

            dateObject = AvailableDate(start_date=date_from, end_date=date_to, property_id=object.id)
            db.add(dateObject)
            db.commit()


def seedPhotos(db: Session, rows: int = 10):
    print("Generating photos...")

    property_ids = [property.id for property in db.query(Property).all()]

    for i in range(0, rows):
        object = Photo(photo=faker.uri(), property_id=faker.random_element(elements=property_ids))
        db.add(object)
        db.commit()


def seedUserMessages(db: Session, rows: int = 10):
    print("Generating User Messages...")

    user_ids = [user.id for user in db.query(User).all()]

    for i in range(0,rows):
        while True:
            send_to = faker.random_element(elements=user_ids)
            send_from = faker.random_element(elements=user_ids)

            if send_to != send_from:
                break

        object = UserMessage(text=faker.paragraph(nb_sentences=3), send_to_id=send_to,
                         user_id=send_from, message_created=faker.date())
        db.add(object)
        db.commit()


def seedPropertyType(db: Session):
    print("Generating property types...")

    property_types = ["Apartment", "House", "Villa", "Cabin", "Cottage", "Mansion"]

    if db.query(PropertyType).count() == 0:
        for name in property_types:
            object = PropertyType(property_type_name=name)
            db.add(object)
            db.commit()
    else:
        print("Property type seeding skipped")


def seedProperties(db: Session, rows: int = 10):
    print("Generating Properties...")

    property_type_ids = [propertytype.id for propertytype in db.query(PropertyType).all()]

    user_ids = [user.id for user in db.query(User).all()]

    for i in range(0, rows):
        # Indoorspace
        indoorspace = IndoorSpace(bed_num=faker.random_int(min=1, max=8), bath_num=faker.random_int(min=1, max=8),
                                  bedroom_num=faker.random_int(min=1, max=5), has_livingroom=faker.pybool(),
                                  total_space=faker.random_int(min=50, max=5000),
                                  description=faker.paragraph(nb_sentences=1),
                                  property_type_id=faker.random_element(elements=property_type_ids))
        db.add(indoorspace)
        db.commit()

        # Location
        location = Location(country=faker.country(), city=faker.city(), address=faker.address(), latitude=faker.latitude(), longitude=faker.longitude())
        db.add(location)
        db.commit()

        object = Property(price=faker.pydecimal(left_digits=3, right_digits=2, positive=True), has_wifi=faker.pybool(),
                          has_airconditioning=faker.pybool(), has_heat=faker.pybool(), has_kitchen=faker.pybool(),
                          has_tv=faker.pybool(), has_parking=faker.pybool(), has_elevator=faker.pybool(),
                          description=faker.paragraph(nb_sentences=3), floor=faker.random_int(min=1, max=10),
                          number_of_guests=faker.random_int(min=1, max=10), is_available=True,
                          user_id=faker.random_element(elements=user_ids), location_id=location.id,
                          indoor_space_id=indoorspace.id, property_created=faker.date(), property_updated=faker.date())
        db.add(object)
        db.commit()

        # Property rule list
        propertyRuleList = PropertyRuleList(smoking_allowed=faker.pybool(), pet_allowed=faker.pybool(),
                                            party_allowed=faker.pybool(),
                                            min_night_number=faker.random_int(min=1, max=20),
                                            property_id=object.id)
        db.add(propertyRuleList)
        db.commit()

        n = faker.random_int(1, 3)

        for j in range(n):
            photo_object = Photo(photo="https://picsum.photos/seed/" + faker.word() + "/410/225", property_id=object.id)
            db.add(photo_object)
            db.commit()

        n = faker.random_int(1, 15)

        for i in range(0, n):
            reviewObject = Review(rating=faker.random_int(min=1, max=5), comment=faker.paragraph(nb_sentences=3))
            db.add(reviewObject)
            db.commit()

            days = faker.random_int(3, 10)
            date_from = faker.date()
            start_date= datetime.strptime(date_from, "%Y-%m-%d")
            end_date = start_date + timedelta(days)
            date_to = end_date.strftime("%Y-%m-%d")



            bookingObject = Booking(start_date=date_from, end_date=date_to,
                                    total_night_num=days,
                                    total_price=faker.pydecimal(left_digits=3, right_digits=2, positive=True),
                                    user_id=faker.random_element(elements=user_ids),
                                    property_id=object.id,
                                    review_id=reviewObject.id, booking_created=faker.date(),
                                    booking_updated=faker.date(), booking_completed=faker.pybool(),booking_verified =faker.pybool())
            db.add(bookingObject)
            db.commit()

        n = faker.random_int(1, 5)

        for i in range(0, n):
            date_from = faker.date()
            start_date = datetime.strptime(date_from, "%Y-%m-%d")
            end_date = start_date + timedelta(days=faker.random_int(3, 10))
            date_to = end_date.strftime("%Y-%m-%d")

            dateObject = AvailableDate(start_date=date_from, end_date=date_to, property_id=object.id)
            db.add(dateObject)
            db.commit()


def seedRoles(db: Session):
    print("Generating roles ... ")

    if db.get(Role, 1) == None:
        role = Role(id=1, role_name='Administrator')
        db.add(role)
        db.commit()

    if db.get(Role, 2) == None:
        role = Role(id=2, role_name='Host')
        db.add(role)
        db.commit()

    if db.get(Role, 3) == None:
        role = Role(id=3, role_name='Renter')
        db.add(role)
        db.commit()


def seedUsers(db: Session, rows: int = 10):
    print("Generating users ... ")

    admin = db.get(Role, 1)
    host = db.get(Role, 2)
    renter = db.get(Role, 3)

    try:
        # Admin
        user = User(username="admin", password=pwd_context.hash("admin"), name=faker.first_name(),
                    lastname=faker.last_name(), email=faker.email(), phone=faker.phone_number(),
                    photo="https://gravatar.com/avatar/123a457f7d531801bd7a1c8b9a07a9c6?s=400&d=robohash&r=x",
                    verified_status=faker.pybool(), user_created=faker.date())
        user.roles.append(admin)
        db.add(user)
        db.commit()
    except Exception as e:
        print("Administration creation skipped")
        db.rollback()

    try:
        # Host
        user = User(username="host", password=pwd_context.hash("host"), name=faker.first_name(),
                    lastname=faker.last_name(), email=faker.email(), phone=faker.phone_number(),
                    photo="https://gravatar.com/avatar/b9b19be737b86ba3eacf535449ead16f?s=400&d=robohash&r=x",
                    verified_status=faker.pybool(), user_created=faker.date())
        user.roles.append(host)
        db.add(user)
        db.commit()
    except Exception as e:
        print("Host creation skipped")
        db.rollback()

    try:
        # Renter
        user = User(username="renter", password=pwd_context.hash("renter"), name=faker.first_name(),
                    lastname=faker.last_name(), email=faker.email(), phone=faker.phone_number(),
                    photo="https://gravatar.com/avatar/b9b19be73abcdea3eacf535449ead16f?s=400&d=robohash&r=x",
                    verified_status=faker.pybool(), user_created=faker.date())
        user.roles.append(renter)
        db.add(user)
        db.commit()
    except Exception as e:
        print("Host creation skipped")
        db.rollback()

    for i in range(0, rows):
        u = faker.user_name()
        h = faker.md5()
        src = "https://gravatar.com/avatar/" + h + "?s=400&d=robohash&r=x"

        user = User(username=u, password=pwd_context.hash(u), name=faker.first_name(), lastname=faker.last_name(),
                    email=faker.email(), phone=faker.phone_number(), photo=src, verified_status=faker.pybool(),
                    user_created=faker.date())

        if i % 3 == 0:
            user.roles.append(admin)

        if i % 3 == 1:
            user.roles.append(host)

        if i % 3 == 2:
            user.roles.append(renter)

        db.add(user)
        db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    seedRoles(db)
    seedUsers(db)
    seedPropertyType(db)
    seedProperties(db, 50)
    seedUserMessages(db,50)
    seedFixedProperties(db,40)
    db.close()
