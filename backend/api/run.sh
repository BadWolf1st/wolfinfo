#!/bin/sh

export SQLALCHEMY_DATABASE_URI=${DATABASE_URL}

PRE_START_PATH=${PRE_START_PATH:-/api/prestart.sh}
echo "Checking for script in $PRE_START_PATH"
if [ -f $PRE_START_PATH ] ; then
    echo "Running script $PRE_START_PATH"
    . "$PRE_START_PATH"
else
    echo "There is no script $PRE_START_PATH"
fi

export APP_MODULE=${APP_MODULE:-src.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8000}
export BACKEND_CORS_ORIGINS=${BACKEND_CORS_ORIGINS}

exec gunicorn --bind $HOST:$PORT "$APP_MODULE" -k uvicorn.workers.UvicornWorker