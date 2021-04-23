FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y upgrade

RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get install -y python3.8
RUN apt-get install -y libeccodes-tools
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-tk
RUN apt-get install -y libproj-dev proj-data proj-bin
RUN apt-get install -y libgeos-dev
RUN apt-get -y install libgl1-mesa-glx
# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

COPY . code

WORKDIR "/code"
CMD ["cd", "code"]
# command to run on container start
CMD [ "python3", "./main.py" ]
