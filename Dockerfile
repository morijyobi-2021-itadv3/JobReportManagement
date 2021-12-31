FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ENV SECRET_KEY `cat /dev/urandom | base64 | fold -w 32 | head -n 1`

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0", "--debugger", "--reload" ]
