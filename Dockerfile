FROM python:3.9.0

WORKDIR /home/

RUN git clone http://www.github.com/grape-git/fragment.git

WORKDIR /home/fragment/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=tj03q1$m*2&amhmwa=7z(r&)ikwh4#()(1&8$u^-_aj-*xxqpk" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]







