FROM python:3.12-alpine3.19

COPY db-populator/requirements/requirements.txt requirements/requirements.txt

# requirements.txt generated via pip-compile -r requirements/requirements.in
RUN python -m pip install -r requirements/requirements.txt

COPY db-populator/src/. .

COPY db-populator/docker-entrypoint.sh docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
