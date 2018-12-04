FROM python:2

WORKDIR /usr/src/app

COPY ./ /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./listen_and_test.py" ]
