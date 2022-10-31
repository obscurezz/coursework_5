from player_base import BasePlayer
from random import randint


class HumanPlayer(BasePlayer):
    def use_attack(self, target: BasePlayer) -> str:
        log_result = []
        if self._check_stamina_for_attack_enough:
            attack_damage = self.weapon.damage * self.unit_class.attack

            if target._check_armor_available():
                target_armor = target.armor * target.unit_class.armor
                log_result.append(f"{target.name} uses his {target.armor.name} to block the attack")
            else:
                target_armor = 0
                log_result.append(f"{target.name}'s {target.armor.name} can't do anything")

            if attack_damage > target_armor:
                ongoing_damage = attack_damage - target_armor
                target.get_damage(ongoing_damage)
                log_result.append(f"{self.name} uses his {self.weapon.name} and deals {ongoing_damage} to {target.name}")
            else:
                log_result.append(f"{self.name} uses his {self.weapon.name} but {target.name} blocks the attack")

            self.current_stamina -= self.weapon.stamina_per_hit

        else:
            log_result.append(f"{self.name} tried to use his {self.weapon.name} but stamina wasn't enough")

        return '\n'.join(log_result)


class CpuPlayer(BasePlayer):
    def use_attack(self, target: BasePlayer) -> str:
        log_result = []
        if not self.unit_class.skill.used:
            if randint(1,2) == 1:
                return self.use_skill(target=target)

        if self._check_stamina_for_attack_enough:
            attack_damage = self.weapon.damage * self.unit_class.attack

            if target._check_armor_available():
                target_armor = target.armor * target.unit_class.armor
                log_result.append(f"{target.name} uses his {target.armor.name} to block the attack")
            else:
                target_armor = 0
                log_result.append(f"{target.name}'s {target.armor.name} can't do anything")

            if attack_damage > target_armor:
                ongoing_damage = attack_damage - target_armor
                target.get_damage(ongoing_damage)
                log_result.append(
                    f"{self.name} uses his {self.weapon.name} and deals {ongoing_damage} to {target.name}")
            else:
                log_result.append(f"{self.name} uses his {self.weapon.name} but {target.name} blocks the attack")

            self.current_stamina -= self.weapon.stamina_per_hit

        else:
            log_result.append(f"{self.name} tried to use his {self.weapon.name} but stamina wasn't enough")

        return '\n'.join(log_result)
