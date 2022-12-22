from kafka import KafkaConsumer

from services import LocationService


TOPIC_NAME = 'locations'
KAFKA_SERVER = 'project07-kafka-0.project07-kafka-headless.default.svc.cluster.local:9092' 

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)


for message in consumer:
    print (message)
    LocationService.create(message)