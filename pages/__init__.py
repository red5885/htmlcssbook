from flask import Blueprint
from .views import *

bp = Blueprint('examples', __name__, url_prefix='/example')

bp.add_url_rule('p20', '/p20', p20)
bp.add_url_rule('p27', '/p27', p27)
bp.add_url_rule('p58', '/p58', p58)
bp.add_url_rule('p140', '/p140', p140)
bp.add_url_rule('p171', '/p171', p171)
bp.add_url_rule('p235', '/p235', p235)