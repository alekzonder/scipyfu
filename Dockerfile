FROM alekzonder/scipython:latest

WORKDIR /app

COPY ./requirements.txt /app
COPY ./server.py /app
COPY ./functions /app/functions

ENV FLASK_APP "server.py"

CMD ["python", "-m", "flask", "run", "-h", "0.0.0.0"]

EXPOSE 5000