from django.contrib import admin
from chat.models import SenderModel, ReceiverModel, ChatModel

admin.site.register(SenderModel)
admin.site.register(ReceiverModel)
admin.site.register(ChatModel)