from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import names
import random

value_schema_str = """
{"namespace": "student.avro",
 "type": "record",
 "doc": "This is an example of Avro.",
 "name": "Student",
 "fields": [
     {"name": "name", "type": ["null", "string"], "default": null, "doc": "Name of the student"},
     {"name": "phone", "type": "int", "default": 1, "doc": "Phone of the student"},
     {"name": "age", "type": "int", "default": 1, "doc": "Age of the student"},
     {"name": "class", "type": "int", "default": 1, "doc": "Class of the student"}
 ]
}
"""

value_schema = avro.loads(value_schema_str)

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.offset()))

avroProducer = AvroProducer({
    'bootstrap.servers': 'peter-kafka01.foo.bar,peter-kafka02.foo.bar,peter-kafka03.foo.bar',
    'on_delivery': delivery_report,
    'schema.registry.url': 'http://peter-kafka03.foo.bar:8081'
    }, default_value_schema=value_schema)

for x in range(5):
    value = {"name": names.get_first_name(), "class": random.randint(1,5), "phone": random.randint(1000,9999), "age": random.randint(10,20)}  # 전송할 메시지
    avroProducer.produce(topic='peter-avro01-kafka1', value=value)

avroProducer.flush()