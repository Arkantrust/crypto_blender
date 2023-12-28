FROM python:alpine AS build

WORKDIR /code

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

FROM build AS staging

RUN adduser -DH -s /bin/sh fastapi

RUN chown -R fastapi:fastapi /code

USER fastapi

FROM staging as production

EXPOSE 80

HEALTHCHECK CMD wget --quiet --tries=1 --spider http://localhost/ || exit 1

COPY words.txt /code/words.txt

COPY ./app /code/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# To run behind a proxy like nginx or traeffik
# CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
