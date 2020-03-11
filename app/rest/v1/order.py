from flask import Blueprint, Response, request

from app.model.order_model import OrderModel

blueprint = Blueprint('order', __name__, url_prefix='/api/v1/order')

# TODO: Awaiting Error Handling and proper implementation


@blueprint.route('/make_order', methods=['POST'])
def make_order():
    request_body = request.get_json()
    order = OrderModel(**request_body).save()
    return {"message": f"Order has been placed with id {order.id}"}, 200


@blueprint.route('/all')
def get_orders():
    orders = OrderModel.objects.to_json()
    return Response(orders, mimetype="application/json", status=200)


@blueprint.route('/find')
def get_order_by_id(order_id):
    order = OrderModel.objects.get(order_id).to_json()
    return Response(order, mimetype="application/json", status=200)