from pathlib import Path

ROOT_PATH = Path(__file__).parent.joinpath()

DATA_PATH = Path.joinpath(ROOT_PATH, 'data')

EQUIP_JSON = Path.joinpath(DATA_PATH, 'equipment.json')
SKILL_JSON = Path.joinpath(DATA_PATH, 'skill.json')
UNIT_JSON = Path.joinpath(DATA_PATH, 'unit_description.json')

RECOVERY_STAMINA_PER_TURN = 1
