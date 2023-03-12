#!//Users/mourkeita/dev/scripts/venv/bin/python3

# coding: utf8

'''
This script receives Rabbitmq messages
'''
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
print("... waiting for messages ...'")

def callback(ch, method, properties, body):
    print("Received %s " % str(body))

channel.basic_consume(on_message_callback=callback, queue='hello')
channel.start_consuming()