FROM python:3.10

WORKDIR /site
COPY . /site

RUN pip install -r /site/requirements.txt

#CMD ["python", "main.py"]
