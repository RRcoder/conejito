import pika

credenciales  = pika.PlainCredentials('root', 'flash')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credenciales))
#connection = pika.BlockingConnection(pika.ConnectionParameters('172.23.0.2'))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")


connection.close()


