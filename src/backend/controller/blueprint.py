from flask import Blueprint

route_bp = Blueprint("route", __name__, url_prefix="/api")

from .route import consultar
