from pydantic import BaseModel
from random import randint


class Weapon(BaseModel):
    name: str
    min_damage: int
    max_damage: int
    stamina_per_hit: int

    @property
    def damage(self):
        return randint(self.min_damage, self.max_damage)

    class Config:
        exclude = ['id']


class Armor(BaseModel):
    name: str
    defence: int
    stamina_per_turn: int

    class Config:
        exclude = ['id']


class EquipData(BaseModel):
    weapons_list: list[dict]
    armor_list: list[dict]
