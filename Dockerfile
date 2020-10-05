#FROM ubuntu:16.04
FROM python:3.6
# Update Software repository
#RUN apt-get update
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
EXPOSE 80
#CMD ["app.py"]
#CMD["pwd"]
#CMD ["gunicorn app:app --workers 16"]
CMD ["gunicorn"  , "-b", "0.0.0.0:80", "app:app"]
