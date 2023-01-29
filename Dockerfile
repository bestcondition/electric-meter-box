FROM python:3.7.15

RUN cd / && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN python3 -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /bestcondition/emb/
