import json
from constants import EQUIP_JSON
from modules.equipment.equip_classes import Weapon, Armor, EquipData


class Equipment:
    """
    Equipment object, implements methods to get equip names and return exact equip
    """
    def __init__(self) -> None:
        self.equipment = self._get_equipment_data

    @staticmethod
    def _get_equipment_data() -> dict:
        """
        :return: json data as dict from equip BaseModel
        """
        with open(EQUIP_JSON, 'r', encoding='utf-8') as equipment_file:
            equipment_raw_data: dict = json.load(equipment_file)
            equipment_schema: EquipData = EquipData(**equipment_raw_data)
            return equipment_schema.dict()

    def get_weapon(self, weapon_name: str) -> Weapon:
        """
        :param weapon_name: name of weapon
        :return: exact weapon by its name
        """
        if weapon_name in self.get_weapon_names():
            weapon_data: list[dict] = self._get_equipment_data()['weapons_list']
            exact_weapon: dict = next(w for w in weapon_data if w['name'] == weapon_name)
            return Weapon(**exact_weapon)
        raise ValueError('No exact weapon available')

    def get_armor(self, armor_name: str) -> Armor:
        """
        :param armor_name: name of armor
        :return: exact armor by its name
        """
        if armor_name in self.get_armor_names():
            armor_data: list[dict] = self._get_equipment_data()['armor_list']
            exact_armor: dict = next(a for a in armor_data if a['name'] == armor_name)
            return Armor(**exact_armor)
        raise ValueError('No exact armor available')

    def get_weapon_names(self) -> list[str]:
        """
        :return: list of all weapons names
        """
        return [w['name'] for w in self._get_equipment_data()['weapons_list']]

    def get_armor_names(self) -> list[str]:
        """
        :return: list of all armors names
        """
        return [a['name'] for a in self._get_equipment_data()['armor_list']]
