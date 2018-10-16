from aiohttp import web
import aiohttp_debugtoolbar
import asyncio
import asyncpg

import click
import logging

from app.utils.data_structures import DBAccessVars
from app.routes import setup_routes

async def add_connection_pool(app, db_access_vars):
    app['pool'] = await asyncpg.create_pool(user=db_access_vars.user,
                                            password=db_access_vars.password,
                                            host=db_access_vars.host,
                                            port=db_access_vars.port,
                                            database=db_access_vars.dbname)
    return app


async def get_app(db_access_vars, debug):

    app = web.Application(debug=debug)
    app = await add_connection_pool(app, db_access_vars)

    setup_routes(app)

    if debug:
        aiohttp_debugtoolbar.setup(app)
    return app


def app_server(port, db_access_vars, debug):
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(get_app(db_access_vars, debug))

    logging.info("Starting webserver...")
    web.run_app(app, port=port)


@click.command()
@click.option('--server-port', envvar='SERVER_PORT', help='Port of the web server', default=8282)
@click.option('--debug/--prod', envvar='DEBUG', help='Switch between production and debug mode', default=False)
@click.option('--db-user', envvar='DB_USER', help='User name for DB access', default='postgres')
@click.option('--db-password', envvar='DB_PASSWORD', help='Password for DB access', default='db')
@click.option('--db-host', envvar='DB_HOST', help='Host URL for DB access', default='0.0.0.0')
@click.option('--db-port', envvar='DB_PORT', help='Port for DB access', default='5432')
@click.option('--db-name', envvar='DB_NAME', help='Name of database', default='postgres')
def main(server_port, debug, db_user, db_password, db_host, db_port, db_name) -> None:
    log_level = logging.INFO if debug is False else logging.DEBUG
    logging.basicConfig(level=log_level)

    db_access_vars = DBAccessVars(user=db_user, password=db_password,
                                  host=db_host, port=db_port, dbname=db_name)
    app_server(server_port, db_access_vars, debug)


if __name__ == '__main__':
    main()

