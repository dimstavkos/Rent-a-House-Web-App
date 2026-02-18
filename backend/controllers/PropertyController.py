import math
import random

from sqlalchemy.orm import Session, joinedload

from Requests.Property.SearchRequest import SearchPropertyRequest
from models.Booking import Booking
from models.IndoorSpace import IndoorSpace
from models.Location import Location
from models.PropertyType import PropertyType
from models.UserViewsProperty import UserViewsProperty
from models.AvailableDate import AvailableDate
from models.Photo import Photo
from models.ReviewView import ReviewView
from models.Property import Property
from models.User import User
from sqlalchemy import or_, and_

class PropertyController:

    def withOptions(self, x):
        x = x.options(joinedload(Property.location, innerjoin=True))\
            .options(joinedload(Property.indoorspace, innerjoin=True).options(joinedload(IndoorSpace.property_type, innerjoin=True)) )\
            .options(joinedload(Property.rules, innerjoin=True)) \
            .options(joinedload(Property.availableDates)) \
            .options(joinedload(Property.photos)) \
            .options(joinedload(Property.review_score)) \
            .options(joinedload(Property.owner))

        return x


    def list(self, db: Session):
        return self.withOptions(db.query(Property)).all()

    def findByid(self, db: Session, id: int):
        return self.withOptions(db.query(Property)).options(joinedload(Property.booking).options(joinedload(Booking.review))).get(id)

    def findByUserid(self, db: Session, user_id: int):
       return self.withOptions(db.query(Property)).filter_by(user_id=user_id).all()

    def delete(self, db: Session, id: int):
        db.query(Property).filter_by(id=id).delete()
        db.commit()
        return "success"

    def create(self, db: Session, entity: Property):
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def search(self, db: Session, request: SearchPropertyRequest):
        query = db.query(Property)

        if request.id != None:
            query = query.filter_by(id=request.id)

        if request.price != None:
            query = query.filter_by(price=request.price)

        if request.has_wifi != None:
            query = query.filter_by(has_wifi=request.has_wifi)

        if request.has_airconditioning != None:
            query = query.filter_by(has_airconditioning=request.has_airconditioning)

        if request.has_heat != None:
            query = query.filter_by(has_heat=request.has_heat)

        if request.has_kitchen != None:
            query = query.filter_by(has_kitchen=request.has_kitchen)

        if request.has_tv != None:
            query = query.filter_by(has_tv=request.has_tv)

        if request.has_parking != None:
            query = query.filter_by(has_parking=request.has_parking)

        if request.has_elevator != None:
            query = query.filter_by(has_elevator=request.has_elevator)

            # query = query.filter(Property.location.address.like('%' + request.location + '%'))

        if request.description != None:
            query = query.filter(Property.description.like('%' + request.description + '%'))

        if request.floor != None:
            query = query.filter_by(floor=request.floor)

        if request.number_of_guests != None:
            query = query.filter(Property.number_of_guests >= request.number_of_guests)

        if request.is_available != None:
            query = query.filter_by(is_available=request.is_available)

        if request.user_id != None:
            query = query.filter_by(user_id=request.user_id)

        if request.indoor_space_id != None:
            query = query.filter_by(indoor_space_id=request.indoor_space_id)

        if request.property_created != None:
            query = query.filter_by(property_created=request.property_created)

        if request.property_updated != None:
            query = query.filter_by(property_updated = request.property_updated)

        if request.property_type_id != None:
            query = query.join(Property.indoorspace).filter_by(property_type_id=request.property_type_id)

        my_filters = []
        if request.is_flat != None and request.is_flat == True:
            my_filters.append(IndoorSpace.property_type_id.like(1))

        if request.is_house != None and request.is_house == True:
            my_filters.append(IndoorSpace.property_type_id.like(2))

        if request.is_villa != None and request.is_villa == True:
            my_filters.append(IndoorSpace.property_type_id.like(3))

        if request.is_cabin != None and request.is_cabin == True:
            my_filters.append(IndoorSpace.property_type_id.like(4))

        if request.is_cottage != None and request.is_cottage == True:
            my_filters.append(IndoorSpace.property_type_id.like(5))

        if request.is_manson != None and request.is_manson == True:
            my_filters.append(IndoorSpace.property_type_id.like(6))

        if len(my_filters) > 0:
            query = query.join(Property.indoorspace).filter(or_(*my_filters))

        if request.location != None or request.country != None or request.city != None:
            location_filters = []

            if (request.location != None):
                location_filters.append(Location.address.like('%' + request.location + '%'))
            if (request.country != None):
                location_filters.append(Location.country.like('%' + request.country + '%'))
            if (request.city != None):
                location_filters.append(Location.city.like('%' + request.city + '%'))

            query = query.join(Property.location).filter(and_(*location_filters))

        if request.date_from != None and request.date_to != None:
            date_filters = []
            date_filters.append(AvailableDate.start_date >= request.date_from)
            date_filters.append(AvailableDate.end_date <= request.date_to)
            query = query.join(Property.availableDates).filter(and_(*date_filters))

        print(str(query))

        return self.withOptions(query).order_by(Property.price.desc()).all()

    def patch(self, db: Session, newEntity: Property):
        existingEntity = db.query(Property).get(newEntity.id)

        existingEntity.price = newEntity.price
        existingEntity.has_wifi = newEntity.has_wifi
        existingEntity.has_aircnditioning = newEntity.has_airconditioning
        existingEntity.has_heat = newEntity.has_heat
        existingEntity.has_kitchen = newEntity.has_kitchen
        existingEntity.has_tv = newEntity.has_tv
        existingEntity.has_parking = newEntity.has_parking
        existingEntity.has_elevator = newEntity.has_elevator
        existingEntity.description = newEntity.description
        existingEntity.floor = newEntity.floor
        existingEntity.number_of_guests = newEntity.number_of_guests
        existingEntity.is_available = newEntity.is_available
        existingEntity.user_id = newEntity.user_id
        existingEntity.location_id = newEntity.location_id
        existingEntity.indoor_space_id = newEntity.indoor_space_id
        existingEntity.property_created = newEntity.property_created
        existingEntity.property_updated = newEntity.property_updated

        db.commit()
        db.refresh(existingEntity)
        return existingEntity

    def printMatrix(self, matrix):
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

    def recommend(self, db:Session, user_id: int):
        learning_rate = 0.2
        K = 3
        ITERATION_LIMIT = 10

        rooms =  db.query(Property).all()
        review_view =  db.query(ReviewView).all()
        # print(review_view)

        rows = db.query(User).count()
        cols = db.query(Property).count()
        print('learning rate:' , learning_rate, ', K=',K, ', dimensions: ', rows, 'x', cols)
        X = [[0 for j in range(cols)] for i in range(rows)]
        XX = [[0 for j in range(cols)] for i in range(rows)]
        EIJ = [[0 for j in range(cols)] for i in range(rows)]

        V = [[random.randint(1, 5) for j in range(K)] for i in range(rows)]
        F = [[random.randint(1, 5) for j in range(cols)] for i in range(K)]
        CURRENT_SE = math.inf

        query = db.query(UserViewsProperty)
        query = query.filter(UserViewsProperty.user_id == user_id)
        n = query.count()

        if n > 0:
            for x in review_view:
                i = x.reviewer_id - 1
                j = x.property_id - 1
                X[i][j] = x.rating
        else:
            for x in db.query(UserViewsProperty).all():
                i = x.user_id -1
                j = x.property_id - 1
                X[i][j] = x.frequency

        for loops in range(ITERATION_LIMIT):
            errors = []

            for i in range(rows):
                for j in range(cols):
                    XX[i][j] = sum([V[i][k] * F[k][j] for k in range(K)])
                    EIJ[i][j] = X[i][j] - XX[i][j];
                    errors.append(EIJ[i][j])

            SE = sum([eij*eij for eij in errors])

            if SE < CURRENT_SE:
                CURRENT_SE = SE

                DIF_V = [[0 for j in range(K)] for i in range(rows)]
                DIF_F = [[0 for j in range(cols)] for i in range(K)]

                for i in range(rows):
                    for j in range(cols):
                        for k in range(K):
                            DIF_V[i][k] = DIF_V[i][k] + learning_rate*EIJ[i][j]
                            DIF_F[k][j] = DIF_F[k][j] + learning_rate*EIJ[i][j]

                for i in range(rows):
                    for k in range(K):
                            V[i][k] = V[i][k] + DIF_V[i][k]

                for k in range(k):
                    for j in range(cols):
                            F[k][j] = F[k][j] + DIF_F[k][j]
                continue
            else:
                break

        rankings = {}

        target_row = user_id - 1;
        i = target_row

        for j in range(cols): # for each property ...
            if X[i][j] == 0: # if the user has not rated it yet
                rate = sum([V[i][k] * F[k][j] for k in range(K)])
                property_id = j + 1
                rankings[property_id] = rate

        rankings = sorted(rankings.items(), reverse=True, key=lambda x: x[1])

        rankings = rankings[0:5]

        rooms = [ ]

        for t in rankings:
            id = t[0]
            room = self.withOptions(db.query(Property).options(joinedload(Property.location, innerjoin=True))).get(id)
            rooms.append(room)

        return rooms

    def commitView(self,db:Session,  user_id: int, property_id : int):
        query = db.query(UserViewsProperty)
        query = query.filter(UserViewsProperty.user_id == user_id).filter(UserViewsProperty.property_id == property_id)

        data = query.all()

        if (len(data) == 0):
            entity = UserViewsProperty(user_id = user_id, property_id = property_id, frequency = 1)
            db.add(entity)
            db.commit()
            return entity
        else:
            existingEntity = data[0]
            existingEntity.frequency = existingEntity.frequency + 1

            db.commit()
            db.refresh(existingEntity)
            return existingEntity

