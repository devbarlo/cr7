FROM wjut/crsource1:alpine

#clonning repo 
RUN git clone https://github.com/wjut/crsource1/tree/master.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/Arab/bin:$PATH"

CMD ["python3","-m","userbot"]
