FROM tiangolo/uwsgi-nginx
RUN apt-get update && apt-get install -y bash nano vim
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app/