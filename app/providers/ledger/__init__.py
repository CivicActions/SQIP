import abc

from app.providers.ledger.qldb import QLDBProvider
from app.providers.messaging.rabbitmq import RabbitMQProvider


class Ledger:
    def __init__(self):
        self.__queue = RabbitMQProvider()
        self.__ledger = QLDBProvider()

    @property
    def db(self):
        return self.__ledger

    @property
    def queue(self):
        return self.__queue


