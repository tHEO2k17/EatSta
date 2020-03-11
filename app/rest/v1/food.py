from flask import Response, Blueprint, request

from app.model.food_model import FoodModel

blueprint = Blueprint('food', __name__, url_prefix='/api/v1/food/')


# TODO: Awaiting error handling

@blueprint.route('/add', methods=['POST'])
def add_food():
    request_body = request.get_json()
    food = FoodModel(**request_body).save()
    return {"message": f"Food added with id {food.id}"}, 200


@blueprint.route('/all')
def get_foods():
    foods = FoodModel.objects.to_json()
    return Response(foods, mimetype='application/json', status=200)


@blueprint.route('/find')
def get_food_by_id(food_id):
    foods = FoodModel.objects.get(id=food_id).to_json()
    return Response(foods, mimetype='application/json', status=200)
