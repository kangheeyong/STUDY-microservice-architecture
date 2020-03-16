import json
from collections import defaultdict

from kafka import KafkaProducer, KafkaConsumer

from Feynman.etc.util import get_logger


class Kafka_queue_cunsumer():
    def __init__(self):
        self.topic = 'test'
        self._kc = KafkaConsumer(self.topic,
                                 bootstrap_servers='0.0.0.0:9092',
                                 group_id='test_user',
                                 enable_auto_commit=True,
                                 consumer_timeout_ms=5000)
        self.logger = get_logger('Kafka_consumer')

    def pop(self):
        result = []
        for data in self.kc:
            try:
                v = defaultdict(None, json.loads(data.value))
            except json.JSONDecodeError:
                self.logger.info('topic: {}, offset: {}, timestamp: {} -> not json type... pass...'
                                 .format(data.topic, data.offset, data.timestamp))
                continue
            datatime = data.timestamp
            result.append({'value': v, 'datatime': datatime})
        self.logger.info('Get {} data...'.format(len(result)))
        return result


class Kafka_queue_producer():
    def __init__(self):
        self.topic = 'test'
        self._kp = KafkaProducer(bootstrap_servers='0.0.0.0:9092',
                                 value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        self.logger = get_logger('Kafka_consumer')

    def push(self, data):
        data = list(data) if isinstance(data, dict) else data
        for d in data:
            self._kp.send(self.topic, d)
        self.logger.info('send {} data...'.format(len(data)))
