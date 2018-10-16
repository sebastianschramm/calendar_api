from aiohttp import web
from http import HTTPStatus


async def handler_health_check(request):
    """
    Returns "200" if it's responsive
    """
    return web.json_response(status=HTTPStatus.OK)
