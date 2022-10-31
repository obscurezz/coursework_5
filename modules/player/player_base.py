from __future__ import annotations

from abc import ABC, abstractmethod

from constants import RECOVERY_STAMINA_PER_TURN
from modules.equipment import Armor, Weapon
from modules.unit_class import UnitClass


class BasePlayer(ABC):
    """
    defines abstract player and its methods
    """

    def __init__(self, name: str, unit_class: UnitClass) -> None:
        self.name = name
        self.unit_class = unit_class
        self.current_health: int = unit_class.max_health
        self.current_stamina: int = unit_class.max_stamina
        self.weapon = None
        self.armor = None

    @property
    def show_current_health(self) -> str:
        return f"{self.name} has {self.current_health} HP"

    @property
    def show_current_stamina(self) -> str:
        return f"{self.name} has {self.current_stamina}"

    def equip_weapon(self, weapon: Weapon) -> str:
        self.weapon = weapon
        return f"{self.name} equipped weapon {self.weapon.name}"

    def equip_armor(self, armor: Armor) -> str:
        self.armor = armor
        return f"{self.name} equipped weapon {self.armor.name}"

    def get_damage(self, damage_amount: int) -> int:
        self.current_health -= damage_amount
        return self.current_health

    def _check_stamina_for_skill_enough(self) -> bool:
        return self.current_stamina >= self.unit_class.skill.stamina_cost

    def use_skill(self, target: BasePlayer) -> str:
        if not self.unit_class.skill.used:
            self.unit_class.skill.used = True
            self.current_stamina -= self.unit_class.skill.stamina_cost
            target.current_health -= self.unit_class.skill.damage
            return f"{self.name} used {self.unit_class.skill.name} and did {self.unit_class.skill.damage} to {target.name}"
        return f"Skill {self.unit_class.skill.name} has been already used"

    def _check_stamina_for_attack_enough(self) -> bool:
        return self.current_stamina >= self.weapon.stamina_per_hit

    @abstractmethod
    def use_attack(self, target: BasePlayer) -> str:
        pass

    def recovery_stamina(self, recovery_value: int) -> None:
        recovery_amount = self.current_stamina + recovery_value * self.unit_class.stamina
        if recovery_amount > self.unit_class.max_stamina:
            self.current_stamina = self.unit_class.max_stamina
        else:
            self.current_stamina = recovery_amount

    def _check_armor_available(self) -> bool:
        return self.current_stamina >= self.armor.stamina_per_turn

    def check_player_is_dead(self) -> bool:
        if self.current_health == 0:
            return True
        return False
