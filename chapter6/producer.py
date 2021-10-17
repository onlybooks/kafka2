from confluent_kafka import Producer

broker = 'peter-kafka01.foo.bar, peter-kafka02.foo.bar, peter-kafka03.foo.bar'
topic = 'peter-test06'

p = Producer({'bootstrap.servers': broker,
              'compression.codec': 'lz4',
              'acks': 1})

# create some_data_source
some_data_source = []
for messageCount in range(1, 11):
    some_data_source.append('Apache Kafka is a distributed streaming platform - %d' % messageCount)

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

for data in some_data_source:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce(topic, data.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()