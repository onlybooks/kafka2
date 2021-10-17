from confluent_kafka import Consumer
import socket

hostname = socket.gethostname()
broker = 'peter-kafka01.foo.bar'
group = 'peter-consumer02'
topic = 'peter-test06'

c = Consumer({
    'bootstrap.servers': broker,
    'group.id': group,
    'session.timeout.ms': 30000,
    'group.instance.id': 'consumer-' + hostname,
    'auto.offset.reset': 'earliest'
})
c.subscribe([topic])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    print('Topic: {}, '
          'Partition: {}, '
          'Offset: {}, '
          'Received message: {}'.format(msg.topic(),
                                        msg.partition(),
                                        msg.offset(),
                                        msg.value().decode('utf-8')))
c.close()
