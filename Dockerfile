# ------------------------------------------------------------
# Base/builder layer
# ------------------------------------------------------------

FROM python:3.10-slim-buster AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get -y install default-libmysqlclient-dev python3-dev build-essential

COPY requirements/requirements.txt /tmp/requirements.txt

# add ",sharing=locked" if release should block until builder is complete
RUN --mount=type=cache,target=/root/.cache,sharing=locked,id=pip \
    pip install --upgrade pip pip-tools && \
    pip install -r /tmp/requirements.txt

# ------------------------------------------------------------
# Dev/testing layer
# ------------------------------------------------------------

FROM builder AS release

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /src/

WORKDIR /src/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# ------------------------------------------------------------
# TODO: Add Production notes
# ------------------------------------------------------------
