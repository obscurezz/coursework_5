from __future__ import annotations

from abc import ABC, abstractmethod

from logger import Logger
from modules.equipment import Armor, Weapon
from modules.unit_class import UnitClass


class BasePlayer(ABC):
    """
    defines abstract player and its methods
    """
    def __init__(self, name: str, unit_class: UnitClass) -> None:
        self.name: str = name
        self.unit_class: UnitClass = unit_class
        self.current_health: int = unit_class.max_health
        self.current_stamina: int = unit_class.max_stamina
        self.weapon = None
        self.armor = None

    @property
    def show_current_health(self) -> str:
        """
        :return: current health amount can't be less than 0
        """
        self.current_health = max(self.current_health, 0)
        return f"{self.name} has {self.current_health} HP"

    @property
    def show_current_stamina(self) -> str:
        """
        :return: current stamina amount can't be less than 0
        """
        self.current_stamina = max(self.current_stamina, 0)
        return f"{self.name} has {self.current_stamina}"

    def equip_weapon(self, weapon: Weapon) -> None:
        """
        :param weapon: weapon we chose
        :return: None
        """
        self.weapon = weapon

    def equip_armor(self, armor: Armor) -> None:
        """
        :param armor: armor we chose
        :return: None
        """
        self.armor = armor

    def get_damage(self, damage_amount: int) -> int:
        """
        :param damage_amount: amount of damage the player gets
        :return: current amount of HP
        """
        self.current_health -= damage_amount
        return self.current_health

    def _check_stamina_for_skill_enough(self) -> bool:
        """
        :return: is stamina for action enough or not
        """
        return self.current_stamina >= self.unit_class.skill.stamina_cost

    def use_skill(self, target: BasePlayer) -> None:
        """
        :param target: enemy that will get damage from skill
        :return: None
        """
        if self.unit_class.skill.used:
            Logger().add_message(f"Skill {self.unit_class.skill.name} has been already used")

        if self._check_stamina_for_attack_enough():
            self.unit_class.skill.used = True
            self.current_stamina -= self.unit_class.skill.stamina_cost
            target.get_damage(self.unit_class.skill.damage)
            Logger().add_message(
                f"{self.name} used {self.unit_class.skill.name} and did {self.unit_class.skill.damage} to {target.name}")

    def _check_stamina_for_attack_enough(self) -> bool:
        """
        :return: is stamina for attack enough or not
        """
        return self.current_stamina >= self.weapon.stamina_per_hit

    @abstractmethod
    def use_attack(self, target: BasePlayer) -> str:
        """
        :param target: enemy that will get damage from attack
        :return: message to log about this action
        """
        pass

    def recovery_stamina(self, recovery_value: int) -> None:
        """
        :param recovery_value: amount of recovered stamina
        :return: None
        """
        recovery_amount = self.current_stamina + recovery_value * self.unit_class.stamina
        if recovery_amount > self.unit_class.max_stamina:
            self.current_stamina = self.unit_class.max_stamina
        else:
            self.current_stamina = recovery_amount

    def _check_armor_available(self) -> bool:
        """
        :return: is stamina enough to use armor
        """
        return self.current_stamina >= self.armor.stamina_per_turn

    def check_player_is_dead(self) -> bool:
        """
        :return: checks HP > 0 or not
        """
        if self.current_health == 0:
            return True
        return False
