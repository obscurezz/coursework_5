from pathlib import Path

# parent directory
ROOT_PATH = Path(__file__).parent.joinpath()
# directory with json files
DATA_PATH = Path.joinpath(ROOT_PATH, 'data')
# html templates
TEMPLATE_PATH = Path.joinpath(ROOT_PATH, 'templates')
# jsons
EQUIP_JSON = Path.joinpath(DATA_PATH, 'equipment.json')
SKILL_JSON = Path.joinpath(DATA_PATH, 'skill.json')
UNIT_JSON = Path.joinpath(DATA_PATH, 'unit_description.json')
# global variable for stamina recovery
RECOVERY_STAMINA_PER_TURN = 1
