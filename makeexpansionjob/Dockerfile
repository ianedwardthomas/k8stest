FROM python:3
ENV PYTHONUNBUFFERED 1

MAINTAINER Ian Thomas <ianedwardthomas@gmail.com>

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt && pip freeze > /intalled_packages.txt

COPY makejobs.py /usr/src/app

ENTRYPOINT ["python", "makejobs.py"]

