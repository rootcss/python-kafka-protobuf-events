### Publishing protobuf based events into Kafka (python)

```bash
# generating the code from proto schemas
./protoc -I=. --python_out=api ./protos/user_created_event.proto
./protoc -I=. --python_out=api ./protos/models/user.proto

# running the publisher and consumer
cd api && python publisher.py
cd kafka-consumer-service && python consumer.py
```
