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

# Установка необходимых пакетов
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv wget && \
    apt-get clean

# Создание и настройка виртуальной среды
RUN python3 -m venv /opt/venv

# Активируем виртуальную среду
ENV PATH="/opt/venv/bin:$PATH"

# Установка pip и selenium в виртуальной среде
RUN pip install --upgrade pip && \
    pip install selenium

# Удаление временных файлов
RUN rm -f get-pip.py

# Установка рабочего каталога
WORKDIR /app