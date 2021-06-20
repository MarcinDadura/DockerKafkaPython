from confluent_kafka import Producer
from time import sleep
import random
sleep(25)
kafka_broker='broker:9092'

topic = 'temp'

config = {
    'bootstrap.servers': kafka_broker,
}

def message(error, msg):
    if error is not None:
        print("Error with message!")
    else:
        print("Temperatura: " + str(msg.value())) 
if __name__=="__main__":
    p=Producer(config)
    while True:
        p.poll(0)
        p.produce(topic, str(random.randint(0,100)), callback=message)
        sleep(random.randint(1,10))
    p.flush()

