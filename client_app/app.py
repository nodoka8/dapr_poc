import grpc
import requests
import helloworld_pb2
import helloworld_pb2_grpc
import time

# def call_grpc_service():
#     with grpc.insecure_channel('grpc_service:50051') as channel:
#         stub = helloworld_pb2_grpc.GreeterStub(channel)
#         response = stub.SayHello(helloworld_pb2.HelloRequest(name='gRPC'))
#     print("gRPC Service Response: " + response.message)

def call_grpc_service():
    with grpc.insecure_channel('dapr_client_app:50003') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        metadata = (('dapr-app-id', 'grpc_service'),)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='grpc'), metadata=metadata)
    print("gRPC Service Response: " + response.message)




def call_http_service():
    #response = requests.get('http://http_service:5000/hello', params={'name': 'HTTP'})
    response = requests.get('http://dapr_client_app:3502/v1.0/invoke/http_service/method/hello', params={'name': 'HTTP'})

    print("HTTP Service Response: " + response.json()['message'])

if __name__ == '__main__':
    time.sleep(10)  # Wait for 20 seconds
    call_grpc_service()
    call_http_service()