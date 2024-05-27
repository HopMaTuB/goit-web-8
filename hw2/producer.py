import pika
import mongoengine as me
from models import Contact
from faker import Faker

me.connect('contacts_db')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

fake = Faker()

def create_fake_contacts(n):
    contacts = []
    for _ in range(n):
        contact = Contact(
            full_name=fake.name(),
            email=fake.email(),
            info=fake.address()
        )
        contact.save()
        contacts.append(contact)
    return contacts

def send_contacts_to_queue(contacts):
    for contact in contacts:
        channel.basic_publish(
            exchange='',
            routing_key='email_queue',
            body=str(contact.id)
        )
        print(f'Sent contact {contact.id} to queue')

if __name__ == '__main__':
    contacts = create_fake_contacts(10)
    send_contacts_to_queue(contacts)
    connection.close()
