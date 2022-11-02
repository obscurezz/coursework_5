from modules.player import BasePlayer
from constants import RECOVERY_STAMINA_PER_TURN
from decorator import singleton
from logger import Logger


@singleton
class Battleground:
    player = None
    enemy = None
    game_is_running = False
    stamina_recovery = RECOVERY_STAMINA_PER_TURN

    @property
    def get_heroes(self) -> dict:
        return {'player': self.player, 'enemy': self.enemy}

    def add_player(self, player: BasePlayer) -> None:
        self.player = player

    def add_enemy(self, enemy: BasePlayer) -> None:
        self.enemy = enemy

    def reset_battleground(self):
        self.__init__()

    def start_game(self) -> None:
        Logger().add_message("The game has begun!")
        self.game_is_running = True

    def _check_players_hp(self) -> None:
        if True in [self.player.check_player_is_dead, self.enemy.check_player_is_dead]:
            self.game_is_running = False

    def _regenerate_players_stamina(self) -> None:
        if self.game_is_running:
            self.player.recovery_stamina(self.stamina_recovery)
            self.enemy.recovery_stamina(self.stamina_recovery)

    def next_turn(self) -> None:
        self._check_players_hp()
        if self.game_is_running:
            self._regenerate_players_stamina()
            self.enemy.use_attack(target=self.player)
        else:
            self.end_game()

    def skip_turn(self) -> None:
        if self.game_is_running:
            Logger().add_message(f"{self.player.name} skipped his turn")
            self.next_turn()

    def player_attack(self) -> None:
        if self.game_is_running:
            self.player.use_attack(target=self.enemy)
            self.next_turn()

    def player_use_skill(self) -> None:
        if self.game_is_running:
            self.player.use_skill(target=self.enemy)
            self.next_turn()

    def end_game(self) -> None:
        self.game_is_running = False

        if self.player.check_player_is_dead():
            Logger().add_message(f"{self.player.name} was defeated.")
        elif self.enemy.check_player_is_dead():
            Logger().add_message(f"{self.enemy.name} was defeated.")
        else:
            Logger().add_message("Draw")
