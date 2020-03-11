from flask import Response, Blueprint
from app.model.status_model import StatusModel

blueprint = Blueprint('status', __name__, url_prefix='/api/v1/status/')


@blueprint.route('/pre_init_status', methods=['POST'])
def generate_status():
    status_array = [StatusModel(**{"name": "ACTIVE", "description": "If item can be used"}),
                    StatusModel(**{"name": "SUSPENDED", "description": "If item is temporarily unavailable"}),
                    StatusModel(**{"name": "INACTIVE", "description": "If item is indefinitely unavailable"}),
                    StatusModel(**{"name": "AWAITING ORDER", "description": "If staff hasn't ordered yet"}),
                    StatusModel(**{"name": "ORDERED", "description": "If staff has ordered"}),
                    StatusModel(**{"name": "SERVED", "description": "If staff has been served"})]

    statuses = StatusModel.objects.insert(status_array).save()

    return {'status': 'Successful', 'message': str(statuses)}, 200


@blueprint.route('/all')
def get_all_status():
    statuses = StatusModel.objects().to_json()
    return Response(statuses, mimetype='application/json', status=200)
