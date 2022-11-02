from flask import Blueprint, render_template
from constants import TEMPLATE_PATH
from modules.battleground.battleground import Battleground

index_blueprint = Blueprint('index_blueprint', __name__, template_folder=TEMPLATE_PATH)


@index_blueprint.get('/')
def index():
    """
    clears battleground for new battle
    :return: start page html
    """
    Battleground().reset_battleground()
    return render_template('index.html')
