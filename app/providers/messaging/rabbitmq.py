from flask.views import MethodView


class RabbitMQProvider(MethodView):

    def get(self):
        return 'Messaging: v0.0.1'
        pass

    def post(self):
        # create a provider instance
        pass
