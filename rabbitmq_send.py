#!//Users/mourkeita/dev/scripts/venv/bin/python3

# coding: utf8

'''
This script sends Rabbitmq messages
'''
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body="It's Mour ...")
print("Sent 'Hello World'")
connection.close()