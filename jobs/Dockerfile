FROM python:3
WORKDIR /usr/src/jobs
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./job.py .
CMD [ "python", "./job.py" ]