from flask import Response, Blueprint, request

from app.model.vendor_model import VendorModel

blueprint = Blueprint('vendor', __name__, url_prefix='/api/v1/vendor/')


@blueprint.route('/add', methods=['POST'])
def add_vendor():
    request_body = request.to_json()
    vendor = VendorModel(**request_body).save()
    return {"message": f"Vendor added with an ID of {vendor.id}"}, 200


@blueprint.route('/all')
def get_vendors():
    vendors = VendorModel.objects.to_json()
    return Response(vendors, mimetype='application/json', status=200)


@blueprint.route('/find')
def get_vendor_by_id(vendor_id):
    vendor = VendorModel.objects.get(vendor_id).to_json()
    return Response(vendor, mimetype='application/json', status=200)
