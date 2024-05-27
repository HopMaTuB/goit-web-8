
import pika
import mongoengine as me
from models import Contact

me.connect('contacts_db')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

def send_email_stub(contact):
    print(f"Sending email to {contact.email}...")
    print(f"Email sent to {contact.email}")

def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first()
    if contact:
        send_email_stub(contact)
        contact.message_sent = True
        contact.save()
        print(f"Updated contact {contact.id}, message_sent: {contact.message_sent}")

channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
