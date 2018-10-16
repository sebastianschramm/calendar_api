FROM python:3-alpine3.6

LABEL maintainer="Sebastian Schramm"

RUN apk update

# hack to keep container small
# ! asyncpg version needs to be the same as in requirements.txt!
RUN apk add --no-cache gcc linux-headers musl-dev libstdc++ lapack g++ gfortran && \
    pip3 install --no-cache-dir asyncpg==0.17.0 && \
    apk del gcc linux-headers musl-dev g++ gfortran

RUN mkdir -p /opt/app
WORKDIR /opt/app

# Install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /opt/app

ENV PATH "/opt/app:${PATH}"

ENTRYPOINT ["python3",  "__main__.py"]

