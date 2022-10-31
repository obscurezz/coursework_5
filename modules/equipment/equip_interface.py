import json
from typing import TextIO
from constants import EQUIP_JSON
from modules.equipment.equip_classes import Weapon, Armor, EquipData


class Equipment:
    def __init__(self) -> None:
        self.equipment = self._get_equipment_data

    @staticmethod
    def _get_equipment_data() -> dict:
        equipment_file: TextIO = open(EQUIP_JSON)
        equipment_raw_data: dict = json.load(equipment_file)
        equipment_schema: EquipData = EquipData(**equipment_raw_data)
        return equipment_schema.dict()

    def get_weapon(self, weapon_name: str) -> Weapon:
        if weapon_name in self.get_weapon_names():
            weapon_data: list[dict] = self._get_equipment_data()['weapons_list']
            exact_weapon: dict = next(w for w in weapon_data if w['name'] == weapon_name)
            return Weapon(**exact_weapon)
        raise ValueError('No exact weapon available')

    def get_armor(self, armor_name: str) -> Armor:
        if armor_name in self.get_armor_names():
            armor_data: list[dict] = self._get_equipment_data()['armor_list']
            exact_armor: dict = next(a for a in armor_data if a['name'] == armor_name)
            return Armor(**exact_armor)
        raise ValueError('No exact armor available')

    def get_weapon_names(self) -> list[str]:
        return [w['name'] for w in self._get_equipment_data()['weapons_list']]

    def get_armor_names(self) -> list[str]:
        return [a['name'] for a in self._get_equipment_data()['armor_list']]
