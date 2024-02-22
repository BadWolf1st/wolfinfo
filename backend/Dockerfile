FROM python:3.11.4-slim-buster as development_build

RUN addgroup --system api && adduser --system --group api

ARG API_ENV

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONFAULTHANDLER=1
ENV	PYTHONUNBUFFERED=1
ENV	PYTHONHASHSEED=random

ENV	PIP_NO_CACHE_DIR=off
ENV	PIP_DISABLE_PIP_VERSION_CHECK=on
ENV	PIP_DEFAULT_TIMEOUT=100

ENV POETRY_VERSION=1.7.1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR='/var/cache/pypoetry'

# System deps:
RUN apt-get update \
	&& apt-get install --no-install-recommends -y \
		bash \
		build-essential \
		curl \
		gettext \
		git \
		libpq-dev \
		wget \
	&& apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
	&& pip install idna \
	&& pip install "poetry==$POETRY_VERSION" && poetry --version

WORKDIR /api/

COPY ./api/pyproject.toml ./api/poetry.lock* /api/

ARG INSTALL_DEV=false

RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

RUN poetry install

COPY ./api /api

ENV PYTHONPATH=/api

RUN chown -R api:api $HOME

USER api

RUN chmod u+x run.sh

CMD ["./run.sh"]