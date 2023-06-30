FROM ubuntu
COPY * .
RUN apt-get --assume-yes update
RUN apt-get --assume-yes install python3-pip 
RUN apt-get --assume-yes install nginx
RUN pip install -r requirements.txt
COPY nginx.conf /etc/nginx/nginx.conf
CMD service nginx restart && gunicorn app.main:app
