import time

from Feynman.database import Kafka_queue_consumer


if __name__ == '__main__':
    a = Kafka_queue_consumer('config.json')
    while True:
        d = a.pop()
        time.sleep(120)
