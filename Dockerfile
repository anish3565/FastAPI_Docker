FROM python:3.12.3-slim

RUN pip install fastapi uvicorn

WORKDIR /app

COPY endpoint.py .

EXPOSE 8000

CMD ["uvicorn", "endpoint:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]