FROM ubuntu:17.10
LABEL maintainer="nicolas@hired.com"

# ENV DEBIAN_FRONTEND noninteractive
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN apt-get update
RUN apt-get install -y python3.7 python3-pip nginx supervisor
RUN pip3 install spacy
RUN pip3 install gunicorn
RUN pip3 install gensim

RUN python3 -m spacy download en
RUN python3 -m gensim.downloader --download glove-twitter-200

# Setup flask application
RUN mkdir -p /deploy/focus
COPY . /deploy/focus
WORKDIR /deploy/focus
RUN bash install.sh
RUN pip3 install -e .
WORKDIR /

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY gunicorn.conf /etc/supervisor/conf.d/gunicorn.conf

# Start processes
CMD ["/usr/bin/supervisord"]
