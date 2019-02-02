from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from mainmodule.services import getUserConfig

#WebSocket consumer - Ref : https://channels.readthedocs.io/en/stable/tutorial/part_1.html

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        userEmail = text_data_json['userEmail']
        print("consumers --> recieved " + message + " from "+userEmail)
        #Get avatar for userEmail from DB.
        userConfig = getUserConfig(userEmail)
        userAvatar = None
        if userConfig is not None:
           userAvatar = userConfig.avatar
        else:
           userAvatar = "No image"
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'userEmail': userEmail,
                'userAvatar' : userAvatar
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        print("chat_message entered")
        message = event['message']
        userEmail = event['userEmail']
        userAvatar = event['userAvatar']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
			'userEmail' : userEmail,
            'userAvatar' : userAvatar
        }))