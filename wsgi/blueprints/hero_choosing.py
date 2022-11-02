from flask import Blueprint, request, render_template, redirect, url_for
from constants import TEMPLATE_PATH
from modules.player.player_type import HumanPlayer, CpuPlayer
from modules.unit_class.unit_class import unit_classes
from modules.equipment.equip_interface import Equipment
from modules.battleground.battleground import Battleground


choose_blueprint = Blueprint('choose_blueprint', __name__, template_folder=TEMPLATE_PATH)

equipment = Equipment()
info: dict = {
    "header": 'Temporary header',
    "classes": list(unit_classes.keys()),
    "weapons": equipment.get_weapon_names(),
    "armors": equipment.get_armor_names()
}


@choose_blueprint.get('/choose-hero/')
def choose_hero():
    """
    choose unit class, armor and weapon for human player
    :return:
    """
    info['header'] = 'Choose your hero'
    return render_template('hero_choosing.html', result=info)


@choose_blueprint.post('/choose-hero/')
def create_hero():
    """
    choose unit class, armor and weapon for human player
    :return:
    """
    player = request.values
    player_fulfilled = HumanPlayer(name=player['name'], unit_class=unit_classes[player['unit_class']])
    player_fulfilled.equip_weapon(equipment.get_weapon(player['weapon']))
    player_fulfilled.equip_armor(equipment.get_armor(player['armor']))
    Battleground().add_player(player_fulfilled)
    return redirect(url_for('choose_blueprint.choose_enemy'))


@choose_blueprint.get('/choose-enemy/')
def choose_enemy():
    """
    choose unit class, armor and weapon for cpu player
    :return:
    """
    info['header'] = 'Choose your enemy'
    return render_template('hero_choosing.html', result=info)


@choose_blueprint.post('/choose-enemy/')
def create_enemy():
    """
    choose unit class, armor and weapon for cpu player
    :return:
    """
    enemy = request.values
    enemy_fulfilled = CpuPlayer(name=enemy['name'], unit_class=unit_classes[enemy['unit_class']])
    enemy_fulfilled.equip_weapon(equipment.get_weapon(enemy['weapon']))
    enemy_fulfilled.equip_armor(equipment.get_armor(enemy['armor']))
    Battleground().add_enemy(enemy_fulfilled)
    return redirect(url_for('fight_blueprint.fight'))
