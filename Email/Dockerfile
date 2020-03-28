FROM python:3
WORKDIR /usr/src/Email
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./emailSearch.py .
CMD [ "python", "./emailSearch.py" ]

