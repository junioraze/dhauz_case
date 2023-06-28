FROM python:3.9.1

WORKDIR /app
COPY ["requirements.txt", "result.py", "queries.py", ".env", "./"]
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "result.py" ]