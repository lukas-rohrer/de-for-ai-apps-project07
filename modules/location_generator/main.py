import time
from concurrent import futures

import grpc
import location_pb2
import location_pb2_grpc

from kafka import KafkaProducer

TOPIC_NAME = 'locations'
KAFKA_SERVER = 'project07-kafka-0.project07-kafka-headless.default.svc.cluster.local:9092' 


producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)



class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):

        request_value = {
            "person_id": request.person_id,
            "latitude": request.latitude,
            "longitude": request.longitude
        }
        producer.send(TOPIC_NAME, request_value)
        producer.flush()
        print(request_value)

        return location_pb2.LocationMessage(**request_value)


# Intiialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# keep thread alive
try: 
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)