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
## notes
- the maximum size of a message Kafka: 1MB
- unbalanced cluster: add new brokers to an existing Kafka cluster. However, these brokers will not be allocated any data partitions from the cluster's existing topics, so they won't be performing much work unless the partitions are moved or new topics are formed. A cluster is referred to as an unbalanced
