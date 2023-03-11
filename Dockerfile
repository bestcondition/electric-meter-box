FROM python:3.7.15

WORKDIR /app
CMD ["python3", "main.py"]
RUN cd / && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY src /app
