from flask_restx import Namespace, fields, Resource

from app.providers.ledger import Ledger

SqipApi = Namespace('publish', description='publish a ledger entry')

cat = SqipApi.model('entry', {
    'id': fields.String(required=True, description='A unique ID'),
    'data': fields.String(required=True, description='JSON data blob'),
})

ledger = Ledger()


@SqipApi.route('/version')
class Version(Resource):
    @SqipApi.doc('Get the API version')
    def get(self):
        return '0.0.1'


@SqipApi.route('/health')
class Health(Resource):
    @SqipApi.doc('Get the API health')
    def get(self):
        return 'OKAY'


@SqipApi.route('/start')
class Start(Resource):
    @SqipApi.doc('Start the service')
    def post(self):
        ledger.db.connect()
        ledger.queue.connect()
        return 'OKAY'


@SqipApi.route('/stop')
class Stop(Resource):
    @SqipApi.doc('Stop the Service')
    def post(self):
        ledger.db.disconnect()
        ledger.queue.disconnect()
        return 'OKAY'


