FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
EXPOSE 80
ENV FLASK_APP=main.py
CMD ["flask", "run", "--host=0.0.0.0"]