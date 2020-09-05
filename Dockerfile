FROM python

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

# RUN mkdir c:\home\speedtest

# COPY main.py /home/speedtest/main.py

# COPY result.csv /home/speedtest/result.csv

CMD python main.py
