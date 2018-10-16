import json
import logging
from http import HTTPStatus

from aiohttp import web


from app.db.psql_statements import GET_MATCHES
from app.schemas import MatchSchema
from app.utils.data_structures import MatchInput

async def get_matches(request):
    """
    Returns a list of matches
    """
    try:
        payload = await request.json()
        logging.info(payload)
        match_input = MatchInput(**payload)
    except json.decoder.JSONDecodeError:
        return web.json_response(status=HTTPStatus.BAD_REQUEST)

    pool = request.app['pool']
    schema = MatchSchema()

    async with pool.acquire() as conn:
        list_of_matches = await conn.fetch(GET_MATCHES,
                                           match_input.candidate_id,
                                           (match_input.interviewers_ids,))
    list_of_matches = [schema.dump(schema.load(user).data).data for user in list_of_matches]
    return web.json_response({"available_time_slots": list_of_matches})

