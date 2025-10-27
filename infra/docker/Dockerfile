From python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install

COPY . /app/

EXPOSE 8000

CMD ["uvicorn", "api.endpoint_router:app", "--host", "0.0.0.0", "--port", "8000"]










