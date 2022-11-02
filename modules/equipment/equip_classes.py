from random import randint
from pydantic import BaseModel


class Weapon(BaseModel):
    """
    Implements weapon model, with its name, damage parameters and stamina needed
    """
    name: str
    min_damage: int
    max_damage: int
    stamina_per_hit: int

    @property
    def damage(self) -> int:
        """
        :return: random damage between min and max
        """
        return randint(self.min_damage, self.max_damage)

    class Config:
        """
        Excludes ID row from json to create object
        """
        exclude = ['id']


class Armor(BaseModel):
    """
    Implements armor model, with its name, defence parameters and stamina needed
    """
    name: str
    defence: int
    stamina_per_turn: int

    class Config:
        """
        Excludes ID row from json to create object
        """
        exclude = ['id']


class EquipData(BaseModel):
    """
    Implements lists of available weapons and armors
    """
    weapons_list: list[dict]
    armor_list: list[dict]
