import time

from Feynman.database import Kafka_queue_producer


if __name__ == '__main__':
    a = Kafka_queue_producer('config.json')
    while True:
        try:
            data = [{'test': 'test'} for _ in range(0, 3)]
            a.push(data)
            time.sleep(30)

            a.push(['dfdfsdf'])
            time.sleep(30)
        except:
            print('....')
            break
