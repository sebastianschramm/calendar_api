from aiohttp import web

from app.db.psql_statements import GET_CANDIDATES, GET_INTERVIEWERS


async def get_users(request, psql_get: str, response_key: str):
    """
    Returns a list of all existing users
    """
    pool = request.app['pool']

    async with pool.acquire() as conn:
        list_of_users = await conn.fetch(psql_get)
    list_of_users = [dict(user.items()) for user in list_of_users]

    return web.json_response({response_key: list_of_users})


async def get_candidates(request):
    return await get_users(request, GET_CANDIDATES, 'candidates')


async def get_interviewers(request):
    return await get_users(request, GET_INTERVIEWERS, 'interviewers')
