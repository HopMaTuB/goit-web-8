
import mongoengine as me

class Contact(me.Document):
    full_name = me.StringField(required=True)
    email = me.EmailField(required=True)
    message_sent = me.BooleanField(default=False)
    info = me.StringField()
