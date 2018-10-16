from http import HTTPStatus
import json

from aiohttp import web

from app.db.psql_statements import GET_CANDIDATE_TIMES, GET_INTERVIEWER_TIMES, \
                                   INSERT_CANDIDATE_TIMES, INSERT_INTERVIEWER_TIMES
from app.schemas import TimeSlotSchema, TimeSlotWithUserSchema
from app.utils.data_structures import TimeslotsInput


async def get_timeslots(request, psql_get: str, response_key: str):
    """
    Returns a list of timeslots for a given user
    """
    pool = request.app['pool']
    schema = TimeSlotSchema()

    user_id = request.match_info.get('user_id', None)
    if user_id is None:
        return web.json_response(status=HTTPStatus.BAD_REQUEST)
    else:
        user_id = int(user_id)

    async with pool.acquire() as conn:
        list_of_times = await conn.fetch(psql_get, user_id)
    list_of_times = [schema.dump(schema.load(ts).data).data for ts in list_of_times]
    return web.json_response({response_key: list_of_times})


async def get_timeslots_candidates(request):
    return await get_timeslots(request, GET_CANDIDATE_TIMES, 'candidate_times')


async def get_timeslots_interviewers(request):
    return await get_timeslots(request, GET_INTERVIEWER_TIMES, 'interviewer_times')


async def add_timeslots(request, psql_insert: str, response_key: str):
    """
    Inserts a list of timeslots for a given user
    """
    try:
        payload = await request.json()
        timeslots_input = TimeslotsInput(**payload)
    except json.decoder.JSONDecodeError:
        return web.json_response(status=HTTPStatus.BAD_REQUEST)

    pool = request.app['pool']
    schema = TimeSlotWithUserSchema()

    user_id = request.match_info.get('user_id', None)
    if user_id is None:
        return web.json_response(status=HTTPStatus.BAD_REQUEST)
    else:
        user_id = int(user_id)

    times = [schema.load(add_user_field(_, user_id)).data for _ in timeslots_input.timeslots]

    async with pool.acquire() as conn:
        await conn.executemany(psql_insert, times)
    return web.json_response({response_key: "inserted"})


async def add_timeslots_candidates(request):
    return await add_timeslots(request, INSERT_CANDIDATE_TIMES, 'candidate_times')

async def add_timeslots_interviewers(request):
    return await add_timeslots(request, INSERT_INTERVIEWER_TIMES, 'interviewer_times')


def add_user_field(_dict, user_id):
    _dict['user_id'] = user_id
    return _dict
