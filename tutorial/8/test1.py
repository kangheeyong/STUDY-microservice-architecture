import time
import json
from collections import defaultdict

from kafka import KafkaProducer, KafkaConsumer

from Feynman.etc.util import get_logger, Config


class Kafka_queue_consumer():
    def __init__(self, path):
        self._opt = Config(open(path, 'r').read())
        self._kc = KafkaConsumer(self._opt.kafka_test.topic,
                                 bootstrap_servers=self._opt.kafka_test.bootstrap_servers,
                                 group_id=self._opt.kafka_test.group_id,
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=True,
                                 consumer_timeout_ms=5000)
        self.logger = get_logger('Kafka_consumer')

    def pop(self):
        result = []
        for data in self._kc:
            try:
                v = defaultdict(None, json.loads(data.value))
            except Exception as e:
                self.logger.info('topic: {}, offset: {} -> {}... pass...'
                                 .format(data.topic, data.offset, data.timestamp, e))
                continue
            datatime = data.timestamp
            result.append({'value': v, 'datatime': datatime})
        self.logger.info('Get {} data...'.format(len(result)))
        return result


class Kafka_queue_producer():
    def __init__(self, path):
        self._opt = Config(open(path, 'r').read())
        self.topic = self._opt.kafka_test.topic
        self._kp = KafkaProducer(bootstrap_servers=self._opt.kafka_test.bootstrap_servers,
                                 value_serializer=lambda x: json.dumps(x).encode('utf-8'))
        self.logger = get_logger('Kafka_consumer')

    def push(self, data):
        data = list(data) if isinstance(data, dict) else data
        for d in data:
            self._kp.send(self.topic, d)
        self.logger.info('send {} data...'.format(len(data)))


if __name__ == '__main__':
    a = Kafka_queue_producer('config.json')
    while True:
        data = [{'test': 'test'} for _ in range(0, 3)]
        a.push(data)
        time.sleep(30)
