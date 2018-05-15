FROM ubuntu
WORKDIR /usr/src/app
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
COPY stable-req.txt ./
RUN pip install --no-cache-dir -r stable-req.txt
COPY webserver.py ./
RUN chmod +x webserver.py
EXPOSE 5000:5000
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV FLASK_APP webserver.py
# CMD ["FLASK_APP=webserver.py flask run"]
CMD ["which python"]
