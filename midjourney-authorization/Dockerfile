# # source https://github.com/joyzoursky/docker-python-chromedriver/blob/master/py-alpine/3.11-alpine-selenium/Dockerfile

# FROM python:3.11-alpine

# # update apk repo
# RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
#     echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

# # install chromedriver
# # RUN apk update
# # RUN apk add chromium chromium-chromedriver

# # upgrade pip
# RUN pip install --upgrade pip

# RUN pip install webdriver-manager

# # install selenium
# RUN pip install selenium

FROM selenium/standalone-chrome

USER root
RUN apt-get update && apt-get install python3-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN python3 -m pip install selenium