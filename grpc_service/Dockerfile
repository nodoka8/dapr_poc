FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. helloworld.proto
CMD ["python", "server.py"]