import pika
import sys
import os

def main():
    credenciales  = pika.PlainCredentials('root', 'flash')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credenciales))

    channel = connection.channel()

    channel.queue_declare(queue = 'hello')

    def callback(ch, method, properties, body):
        print(f"[x] recibido: {body}")
    
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Esperando por mensajes, presionar control c para finalizar')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrumpido")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

