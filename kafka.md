# kafka
## producer
```python
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='HOSTNAME:9093')
for _ in range(10):
    print(_)
    producer.send('quickstart', b'some_message_bytes')
    producer.flush()

```
## consumer
```python
from kafka import KafkaConsumer


consumer = KafkaConsumer('quickstart',auto_offset_reset="earliest",bootstrap_servers='HOSTNAME:9093')
for msg in consumer:
    print(msg)
```
