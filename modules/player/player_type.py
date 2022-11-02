from modules.player.player_base import BasePlayer
from logger import Logger
from random import randint


class HumanPlayer(BasePlayer):
    def use_attack(self, target: BasePlayer) -> str:
        if self._check_stamina_for_attack_enough:
            attack_damage = self.weapon.damage * self.unit_class.attack

            if target._check_armor_available():
                target_armor = target.armor.defence * target.unit_class.armor
                Logger().add_message(f"{target.name} uses his {target.armor.name} to block the attack")
            else:
                target_armor = 0
                Logger().add_message(f"{target.name}'s {target.armor.name} can't do anything")

            if attack_damage > target_armor:
                ongoing_damage = attack_damage - target_armor
                target.get_damage(ongoing_damage)
                Logger().add_message(f"{self.name} uses his {self.weapon.name} and deals {ongoing_damage} to {target.name}")
            else:
                Logger().add_message(f"{self.name} uses his {self.weapon.name} but {target.name} blocks the attack")

            self.current_stamina -= self.weapon.stamina_per_hit

        else:
            Logger().add_message(f"{self.name} tried to use his {self.weapon.name} but stamina wasn't enough")

        return Logger().get_message()


class CpuPlayer(BasePlayer):
    def use_attack(self, target: BasePlayer) -> str:
        if not self.unit_class.skill.used:
            if randint(1,2) == 1:
                self.use_skill(target=target)
                Logger().add_message(
                    f"{self.name} used {self.unit_class.skill.name} and did {self.unit_class.skill.damage} to {target.name}")
                return Logger().get_message()

        if self._check_stamina_for_attack_enough:
            attack_damage = self.weapon.damage * self.unit_class.attack

            if target._check_armor_available():
                target_armor = target.armor.defence * target.unit_class.armor
                Logger().add_message(f"{target.name} uses his {target.armor.name} to block the attack")
            else:
                target_armor = 0
                Logger().add_message(f"{target.name}'s {target.armor.name} can't do anything")

            if attack_damage > target_armor:
                ongoing_damage = attack_damage - target_armor
                target.get_damage(ongoing_damage)
                Logger().add_message(
                    f"{self.name} uses his {self.weapon.name} and deals {ongoing_damage} to {target.name}")
            else:
                Logger().add_message(f"{self.name} uses his {self.weapon.name} but {target.name} blocks the attack")

            self.current_stamina -= self.weapon.stamina_per_hit

        else:
            Logger().add_message(f"{self.name} tried to use his {self.weapon.name} but stamina wasn't enough")

        return Logger().get_message()
