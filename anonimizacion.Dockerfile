FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1
EXPOSE 5003/tcp

COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/src

CMD [ "flask", "--app", "./src/app/api", "--debug", "run", "--host=0.0.0.0", "--port=5003" ]