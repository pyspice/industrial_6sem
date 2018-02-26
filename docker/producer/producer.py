import pika
from time import sleep

if __name__ == '__main__':                                                      
 
    fin = open('source.txt')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='queue', port=5672))

    channel = connection.channel()
    channel.queue_declare(queue='docker_test')

    for line in fin.readlines():
        line = line.strip()
        channel.basic_publish(exchange='', routing_key='docker_test', body=line)

    fin.close()
    connection.close()