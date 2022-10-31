from modules.player import BasePlayer
from constants import RECOVERY_STAMINA_PER_TURN


class BaseSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Battleground(metaclass=BaseSingleton):
    player = None
    enemy = None
    game_is_running = False
    stamina_recovery = RECOVERY_STAMINA_PER_TURN

    def start_game(self, player: BasePlayer, enemy: BasePlayer) -> str:
        self.player = player
        self.enemy = enemy
        self.game_is_running = True
        return "The game has begun!"

    def _check_players_hp(self) -> None:
        if self.player.check_player_is_dead:
            self._end_game(winner=self.enemy)
        if self.enemy.check_player_is_dead:
            self._end_game(winner=self.player)

    def _regenerate_players_stamina(self) -> None:
        self.player.recovery_stamina(self.stamina_recovery)
        self.enemy.recovery_stamina(self.stamina_recovery)

    def next_turn(self) -> None:
        self._check_players_hp()
        if self.game_is_running:
            self._regenerate_players_stamina()
            self.enemy.use_attack(target=self.player)

    def player_attack(self) -> None:
        self.player.use_attack(target=self.enemy)
        self.next_turn()

    def player_use_skill(self) -> None:
        self.player.use_skill(target=self.enemy)
        self.next_turn()

    def _end_game(self, winner: BasePlayer) -> str:
        self.game_is_running = False
        return f"{winner.name} won! Game is ended!"
