import pytest

from aiohttp import web

from app.routes import setup_routes


@pytest.fixture
async def get_app():

    app = web.Application(debug=True)
    setup_routes(app)

    return app


@pytest.fixture
async def cli(aiohttp_client, get_app):

    app = get_app()
    return await aiohttp_client(app)
