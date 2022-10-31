import json
from pydantic import BaseModel, Field
from constants import SKILL_JSON


class Skill(BaseModel):
    name: str
    damage: int
    stamina_cost: int
    used: bool = Field(default=False)


with open(SKILL_JSON) as desc_file:
    skill_base_data: list[dict] = json.load(desc_file)

DefaultSkill = Skill(**skill_base_data[0])
WarriorSkill = Skill(**skill_base_data[1])
ThiefSkill = Skill(**skill_base_data[2])
MageSkill = Skill(**skill_base_data[3])
