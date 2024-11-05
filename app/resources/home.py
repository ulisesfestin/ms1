from flask import jsonify, Blueprint, request
from opentelemetry import trace

home = Blueprint('home', __name__)
tracer = trace.get_tracer(__name__)

@home.route('/', methods=['GET'])
def index():
    with tracer.start_as_current_span("index_route"):
        my_ip = request.remote_addr
        resp = jsonify({"microservicio": my_ip, "status": "ok"})
        resp.status_code = 200
        return resp

@home.route('/health', methods=['GET'])
def health():
    with tracer.start_as_current_span("health_route"):
        resp = jsonify({"status": "ok"})
        resp.status_code = 200
        return resp

@home.route('/version', methods=['GET'])
def version():
    with tracer.start_as_current_span("version_route"):
        resp = jsonify({"version": "0.0.1"})
        resp.status_code = 200
        return resp