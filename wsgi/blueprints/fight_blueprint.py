from flask import Blueprint, render_template, redirect, url_for
from constants import TEMPLATE_PATH
from modules.battleground.battleground import Battleground
from logger import Logger

fight_blueprint = Blueprint('fight_blueprint', __name__, template_folder=TEMPLATE_PATH)


@fight_blueprint.get('/fight/')
def fight():
    """
    starts battle
    :return: html with battle page
    """
    Battleground().start_game()
    log_message = Logger().get_message()
    return render_template('fight.html', heroes=Battleground().get_heroes, result=log_message)


@fight_blueprint.get('/fight/hit/')
def hit():
    """
    human player hits
    :return: html with battle page
    """
    Battleground().player_attack()
    log_message = Logger().get_message()
    if Battleground().game_is_running:
        return render_template('fight.html', heroes=Battleground().get_heroes, result=log_message)
    return redirect(url_for('fight_blueprint.end_fight'))


@fight_blueprint.get('/fight/use-skill/')
def use_skill():
    """
    human player uses skill
    :return: html with battle page
    """
    Battleground().player_use_skill()
    log_message = Logger().get_message()
    if Battleground().game_is_running:
        return render_template('fight.html', heroes=Battleground().get_heroes, result=log_message)
    return redirect(url_for('fight_blueprint.end_fight'))


@fight_blueprint.get('/fight/pass-turn/')
def pass_turn():
    """
    human player skips turn
    :return: html with battle page
    """
    Battleground().skip_turn()
    log_message = Logger().get_message()
    if Battleground().game_is_running:
        return render_template('fight.html', heroes=Battleground().get_heroes, result=log_message)
    return redirect(url_for('fight_blueprint.end_fight'))


@fight_blueprint.get('/fight/end-fight/')
def end_fight():
    """
    ends battle
    :return: html with battle page
    """
    Battleground().end_game()
    log_message = Logger().get_message()
    return render_template('fight.html', heroes=Battleground().get_heroes, result=log_message)
