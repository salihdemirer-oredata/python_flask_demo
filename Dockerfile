FROM python:3-alpine
RUN apk update && apk add pkgconfig
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python3","main.py"]
