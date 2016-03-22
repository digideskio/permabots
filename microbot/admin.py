from django.contrib import admin
from microbot.models import Message, Chat, Update, User, Bot, Handler, EnvironmentVar, Request, Response, Hook

admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(User)
admin.site.register(Update)
admin.site.register(Bot)
admin.site.register(Handler)
admin.site.register(Request)
admin.site.register(EnvironmentVar)
admin.site.register(Response)
admin.site.register(Hook)