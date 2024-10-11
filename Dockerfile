FROM python:3.11 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11

WORKDIR /tree_menu

COPY --from=requirements-stage /tmp/requirements.txt /tree_menu/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /tree_menu/requirements.txt

COPY ./tree_menu ./tree_menu

COPY ./.env.example ./.env.example

COPY ./setup.sh ./setup.sh

RUN ./setup.sh

CMD ["python", "tree_menu/manage.py", "runserver", "0.0.0.0:8000"]
