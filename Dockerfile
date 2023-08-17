FROM python:3.9 as build

WORKDIR /app

RUN apt-get update && apt-get install -y git

# Install Poetry
RUN pip install poetry==1.2.2

COPY ./pyproject.toml ./poetry.lock /app/
RUN poetry export --without-hashes --format requirements.txt > requirements.txt

FROM tiangolo/uvicorn-gunicorn:python3.9-slim

RUN apt-get update && apt-get install -y git

ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

COPY --from=build /app/requirements.txt /app

RUN pip install -r requirements.txt

COPY ./app /app/app

ENV PORT=8000
ENV FORWARDED_ALLOW_IPS="*"
ENTRYPOINT ["/usr/bin/tini", "--"]

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
# See https://github.com/tiangolo/uvicorn-gunicorn-docker/blob/master/docker-images/python3.7.dockerfile
CMD ["/start.sh"]
