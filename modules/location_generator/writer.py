import grpc
import location_pb2
import location_pb2_grpc

"""
Sample Implementation of a writer that writes messages to gRPC
"""

print("Sending sample payload")
channel = grpc.insecure_channel("localhost:30004")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    person_id=10,
    latitude=-65.228528,
    longitude=96.225832
)

response =  stub.Create(location)