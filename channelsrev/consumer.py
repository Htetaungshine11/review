from channels.generic.websocket import WebsocketConsumer
# from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync
class a(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.group_name = self.scope["url_route"]["kwargs"]["name"]
        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,{
                "type":"msg_sender",
                "test":"hello",
                "ahaha":"adf"
            }
        )
        # print()
    def receive(self,text_data=None,bytes_data=None):
        pass

    def msg_sender(self,event):
        print(event)
        self.send(event['test'])
    def disconnect(self,code):
        self.channel_layer.group_discard(self.group_name,self.channel_name)
        self.close()