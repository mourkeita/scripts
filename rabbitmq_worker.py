#!/usr/bin/python
# coding: utf8

'''
This script receives Rabbitmq tasks
'''
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue_cinq', durable=True)
print('Waiting for messages ...')

def callback(ch, method, properties, body):
    print("Received %r" % body)
    import time
    time.sleep(body.count(0))
    print("Done.")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=3)
channel.basic_consume(on_message_callback=callback, queue='task_queue_cinq')
channel.start_consuming()