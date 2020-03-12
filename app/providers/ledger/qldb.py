from flask.views import MethodView


class QLDBProvider(MethodView):

    def get(self):
        return 'Ledger: v0.0.1'
        pass

    def post(self):
        # create a provider instance
        pass
