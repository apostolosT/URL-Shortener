
FROM python:3.7
ARG BUILD_DIR=shorty-app

WORKDIR /usr/src/app

COPY $BUILD_DIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

# ENV BITLY_TOKEN=<BITLY_TOKEN>
# ENV TINYURL_TOKEN=<TINYURL_TOKEN>

CMD ["python","-u", "run.py"]