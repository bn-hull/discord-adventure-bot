FROM ubuntu:18.04

# installing python and pip
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

# settomg hp,e
ENV HOME /home

# copying files over
COPY adventure_bot/ /home/adventure_bot/
COPY tests/ /tests/adventure_bot/
COPY main.py /home/main.py

# setting up work dir
WORKDIR /home

# setting up python module requirements
COPY requirements.txt /home/requirements.txt
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["main.py"]