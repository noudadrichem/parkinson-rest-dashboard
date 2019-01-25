FROM python:3

COPY . .

RUN pip install -r requirements.txt
RUN pip install psycopg2


CMD ["python", "app.py"]

EXPOSE 5432
EXPOSE 9094
