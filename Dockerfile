FROM python:3.8-slim-buster
# ENV IP=192.168.1.11
ENV IP=localhost
ENV PORT=8082
COPY . ./app
RUN pip install --no-cache-dir -r ./app/requirements.txt

WORKDIR /app

CMD [ "pytest", "-svra" ]