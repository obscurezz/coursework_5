import json
from pydantic import BaseModel, Field
from constants import UNIT_JSON
from modules.skill import WarriorSkill, ThiefSkill, MageSkill, DefaultSkill, Skill


class UnitClass(BaseModel):
    """
    Implements unit type for player
    """
    name: str
    max_health: int
    max_stamina: int
    attack: int
    stamina: int
    armor: int
    skill: Skill = Field(default=DefaultSkill)


with open(UNIT_JSON, 'r', encoding='utf-8') as desc_file:
    unit_base_data: list[dict] = json.load(desc_file)

WarriorClass = UnitClass(**unit_base_data[0], skill=WarriorSkill)
ThiefClass = UnitClass(**unit_base_data[1], skill=ThiefSkill)
MageClass = UnitClass(**unit_base_data[2], skill=MageSkill)

unit_classes = {
    WarriorClass.name: WarriorClass,
    ThiefClass.name: ThiefClass,
    MageClass.name: MageClass
}
