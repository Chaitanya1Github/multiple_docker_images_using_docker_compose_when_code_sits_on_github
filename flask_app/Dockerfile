FROM python:3.8-slim-buster
WORKDIR /app
COPY https://github.com/Chaitanya1Github/single-image/blob/f89af1b5cbd22b57834fba7f6d6a2170a82fc359/flask_app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
