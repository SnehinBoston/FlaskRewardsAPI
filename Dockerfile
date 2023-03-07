FROM python:3.10
EXPOSE 9060
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app
# ENTRYPOINT - LOOK FOR MULTIPLE ENTRYPOINTS
CMD python3 app.py; python3 setup_tables.py;flask run --host 0.0.0.0 -p 9060


# docker run -d -p 9070:9070 --name app -v $(PWD):/app app