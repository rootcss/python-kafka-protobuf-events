from confluent_kafka import Consumer
from protos.user_created_event_pb2 import UserCreatedEvent
from protos.models.user_pb2 import User
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp


TOPIC = 'simpl_events_protobuf'
GROUP_ID = 'test_group_1'


def print_assignment(consumer, partitions):
    print('Assignment:', partitions)


def main():
    conf = {'bootstrap.servers': 'localhost:9092', 'group.id': GROUP_ID, 'session.timeout.ms': 6000, 'auto.offset.reset': 'earliest'}
    kafka = Consumer(**conf)
    kafka.subscribe([TOPIC], on_assign=print_assignment)

    try:
        while True:
            msg = kafka.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                print(msg.error())
            else:
                print(f"[{msg.offset()}] {UserCreatedEvent().FromString(msg.value())}")
    except KeyboardInterrupt:
        print('%% Aborted by user\n')
    finally:
        kafka.close()

main()
