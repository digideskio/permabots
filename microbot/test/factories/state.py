# coding=utf-8
from factory import DjangoModelFactory, SubFactory, Sequence
from microbot.models import State, TelegramChatState, KikChatState
from microbot.test.factories import TelegramChatAPIFactory, TelegramUserAPIFactory, BotFactory, KikChatAPIFactory, KikUserAPIFactory

class StateFactory(DjangoModelFactory):
    class Meta:
        model = State
    bot = SubFactory(BotFactory)
    name = Sequence(lambda n: 'state_%d' % n)
    
class TelegramChatStateFactory(DjangoModelFactory):
    class Meta:
        model = TelegramChatState
    chat = SubFactory(TelegramChatAPIFactory)
    state = SubFactory(StateFactory)
    user = SubFactory(TelegramUserAPIFactory)
    
class KikChatStateFactory(DjangoModelFactory):
    class Meta:
        model = KikChatState
    chat = SubFactory(KikChatAPIFactory)
    state = SubFactory(StateFactory)
    user = SubFactory(KikUserAPIFactory)