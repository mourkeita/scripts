#!/usr/bin/python
# coding: utf8

'''
This script sends Rabbitmq tasks
'''
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue_cinq', durable=True)
message = ''.join(sys.argv[1:]) or 'Mayday mayday'
channel.basic_publish(exchange='',
                      routing_key='task_queue_cinq',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2))
print("Message sent {}".format(message))
connection.close()
