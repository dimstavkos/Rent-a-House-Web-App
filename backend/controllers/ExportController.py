from sqlalchemy.orm import Session

from Requests.Role.SearchRequest import SearchRoleRequest
from Responses.ExportReviewResponse import ExportReviewResponse
from Responses.ExportRoleResponse import ExportRoleResponse
from Responses.ExportUserResponse import ExportUserResponse
from Responses.ExportLocationResponse import ExportLocationResponse
from Responses.ExportPropertyResponse import ExportPropertyResponse
from Responses.ExportIndoorSpaceResponse import ExportIndoorSpaceResponse
from Responses.ExportPropertyTypeResponse import ExportPropertyTypeResponse
from Responses.ExportBookingResponse import ExportBookingResponse
from models.Booking import Booking
from models.Role import Role
from models.User import User
from models.Location import Location
from models.Property import Property
from models.IndoorSpace import IndoorSpace
from models.PropertyType import PropertyType
import json


class ExportController:
    #
    #   Export users
    #
    def user_to_resource(self, user):
        roles = [ExportRoleResponse(id=role.id, role_name=role.role_name) for role in user.roles]
        return ExportUserResponse(id=user.id, username=user.username, name=user.name, lastname=user.lastname,
                                  email=user.email, phone=user.phone, photo=user.photo, roles=roles)

    def exportUsers(self, db: Session, xml: bool):
        users = db.query(User).all()

        resources = [self.user_to_resource(entity) for entity in users]

        if xml:
            resources = [x.dict() for x in resources]
            for x in resources:
                x['roles'] = {
                    "roles": x['roles']
                }
            data = {"user": resources}
            return data
        else:
            data = {"users": resources}

        return data

    #
    #   Export locations
    #

    def location_to_resource(self, location):
        return ExportLocationResponse(id=location.id, country=location.country, city=location.city,
                                      address=location.address)

    def exportLocations(self, db: Session, xml: bool):
        locations = db.query(Location).all()

        resources = [self.location_to_resource(entity) for entity in locations]

        if xml:
            resources = [x.dict() for x in resources]
            # for x in resources:
            #     x['roles'] = {
            #         "roles": x['roles']
            #     }
            data = {"locations": resources}
            return data
        else:
            data = {"locations": resources}

        return data

    #
    #   Export bookings
    #
    def booking_to_resource(self, booking):
        review = booking.review

        if review.details != None:
            review = ExportReviewResponse(id=review.id, rating=review.rating, comment=review.comment, reviewer_id=review.details.review_id,
                                          reviewee_id=review.details.reviewee_id)
        else:
            review = ExportReviewResponse(id=review.id, rating=review.rating, comment=review.comment,
                                          reviewer_id=1,
                                          reviewee_id=3)

        return ExportBookingResponse(id=booking.id, start_date=booking.start_date, end_date=booking.end_date,
                                     total_night_num=booking.total_night_num, total_price=booking.total_price,
                                     user_id=booking.user_id, property_id=booking.property_id, review_id=review,
                                     booking_created=booking.booking_created, booking_updated=booking.booking_updated,
                                     booking_completed=booking.booking_completed)

    def exportBookings(self, db: Session, xml: bool):
        bookings = db.query(Booking).all()

        resources = [self.booking_to_resource(entity) for entity in bookings]

        if xml:
            resources = [x.dict() for x in resources]
            data = {"bookings": resources}
            return data
        else:
            data = {"bookings": resources}

        return data

    #
    #   Export properties
    #
    def property_to_resource(self, property, db: Session):
        location = db.query(Location).filter_by(id=property.location_id).first()
        user = db.query(User).filter_by(id=property.user_id).first()
        indoorSpace = db.query(IndoorSpace).filter_by(id=property.indoor_space_id).first()
        propertyType = db.query(PropertyType).filter_by(id=indoorSpace.property_type_id).first()

        locations = [ExportLocationResponse(id=location.id, country=location.country, city=location.city,
                                            address=location.address)]

        propertyTypeList = [
            ExportPropertyTypeResponse(id=propertyType.id, property_type_name=propertyType.property_type_name)]

        indoorspaceList = [
            ExportIndoorSpaceResponse(id=indoorSpace.id, bed_num=indoorSpace.bed_num, bath_num=indoorSpace.bath_num,
                                      bedroom_num=indoorSpace.bedroom_num, has_livingroom=indoorSpace.has_livingroom,
                                      total_space=indoorSpace.total_space, description=indoorSpace.description,
                                      property_type_id=propertyTypeList)]

        roles = [ExportRoleResponse(id=role.id, role_name=role.role_name) for role in user.roles]
        userList = [ExportUserResponse(id=user.id, username=user.username, name=user.name, lastname=user.lastname,
                                       email=user.email, phone=user.phone, photo=user.photo, roles=roles)]

        return ExportPropertyResponse(id=property.id, price=property.price, has_wifi=property.has_wifi,
                                      has_airconditioning=property.has_airconditioning, has_heat=property.has_heat,
                                      has_kitchen=property.has_kitchen, has_tv=property.has_tv,
                                      has_parking=property.has_parking, has_elevator=property.has_elevator,
                                      description=property.description, floor=property.floor,
                                      number_of_guests=property.number_of_guests, is_available=property.is_available,
                                      user_id=userList, location_id=locations, indoor_space_id=indoorspaceList)

    def exportProperties(self, db: Session, xml: bool):
        properties = db.query(Property).all()

        resources = [self.property_to_resource(entity, db) for entity in properties]

        if xml:
            resources = [x.dict() for x in resources]
            for x in resources:
                x['location_id'] = {
                    "locations": x['location_id']
                }
                x['user_id'] = {
                    "users": x['user_id']
                }
                x['indoor_space_id'] = {
                    "indoor_space": x['indoor_space_id']
                }
            data = {"property": resources}
            return data
        else:
            data = {"property": resources}

        return data

    #
    #   Export ratings
    #
    def exportRatings(self, db: Session):
        return db.query(Role).all()
