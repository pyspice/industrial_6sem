import pika                                      
from pymongo import MongoClient

if __name__ == '__main__':                                               
    db = MongoClient(host='db', port=27017)['docker']

    def callback(channel, method, properties, body):
        global db
        print("message received: {}".format(body), flush=True)   
        db['msgs'].insert({'msg': body})                         
                      
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='queue', port=5672))

    channel = connection.channel()
    channel.queue_declare(queue='docker_test')
              
    channel.basic_consume(callback, queue='docker_test', no_ack=True)
    channel.start_consuming()