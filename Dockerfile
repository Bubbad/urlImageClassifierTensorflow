FROM tensorflow/tensorflow

RUN apt-get update && apt-get install -y --no-install-recommends python-bottle

RUN pip install Pillow

COPY server.py /
COPY classify_image.py /

EXPOSE 8080

WORKDIR "/"

CMD ["python", "server.py"]