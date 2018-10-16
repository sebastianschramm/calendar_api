# Calendar API

WIP

## Getting started

#### Requirements

* Docker
* Docker-compose

#### Run app
In the root of the project run docker-compose to start the app with a postgres DB by e.g.
executing:
```bash
docker-compose -f contrib/docker-compose.yml up --build
```

## Run test
To execute the tests, run the following in the root of the project:
```bash
pytest
```

## API documentation
The API is documented using Swagger Version 2.0 in the file [swagger.yaml](./swagger/swagger.yaml).
A helpful tool to visualize the documentation is [Swagger Editor](https://swagger.io/tools/swagger-editor/).
