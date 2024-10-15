from flask import jsonify, Blueprint, request

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():
    my_ip = request.remote_addr
    resp = jsonify({"microservicio": my_ip, "status": "ok"})
    resp.status_code = 200
    return resp

@home.route('/health', methods=['GET'])
def health():
    resp = jsonify({"status": "ok"})
    resp.status_code = 200
    return resp

@home.route('/version', methods=['GET'])
def version():
    resp = jsonify({"version": "0.0.1"})
    resp.status_code = 200
    return resp