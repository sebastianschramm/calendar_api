import datetime

import asyncpg
import marshmallow as ma

from app.utils.data_structures import TimeslotWithUser


class BaseSchema(ma.Schema):

    @ma.post_load
    def instantiate(self, data):
        assert self.instance_name is not None
        return self.instance_name(**data)


class CustomDateField(ma.fields.Date):
    def _deserialize(self, value, attr, data):
        if isinstance(value, datetime.date):
            return value
        return super()._deserialize(value, attr, data)

    def _serialize(self, value, attr, obj):
        if isinstance(value, datetime.date):
            return value.strftime('%Y-%m-%d')
        return super()._serialize(value, attr, obj)


class RecordToDictMixin(ma.Schema):

    @ma.pre_load
    def format_date(self, data):
        if isinstance(data, asyncpg.Record):
            data = dict(data.items())
        return data


class User(ma.Schema):
    user_id = ma.fields.Int()
    user_name = ma.fields.Str()

class CandidateUser(User):
    pass

class InterviewerUser(User):
    pass


class MatchSchema(RecordToDictMixin, ma.Schema):
    date = CustomDateField()
    start_time = ma.fields.Int()


class TimeSlotSchema(RecordToDictMixin, ma.Schema):
    date = CustomDateField()
    start_time = ma.fields.Int()


class TimeSlotWithUserSchema(BaseSchema):
    instance_name = TimeslotWithUser

    date = ma.fields.Date()
    start_time = ma.fields.Int()
    user_id = ma.fields.Int()
