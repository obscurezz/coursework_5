from modules.player import BasePlayer
from constants import RECOVERY_STAMINA_PER_TURN
from decorator import singleton
from logger import Logger


@singleton
class Battleground:
    """
    Singleton arena for players fight implementation
    """
    player: None | BasePlayer = None
    enemy: None | BasePlayer = None
    game_is_running: bool = False
    stamina_recovery: int = RECOVERY_STAMINA_PER_TURN

    @property
    def get_heroes(self) -> dict:
        """
        :return: dictionary with player and enemy objects as values
        """
        return {'player': self.player, 'enemy': self.enemy}

    def add_player(self, player: BasePlayer) -> None:
        """
        :param player: human player
        :return: None
        """
        self.player = player

    def add_enemy(self, enemy: BasePlayer) -> None:
        """
        :param enemy: cpu player
        :return: None
        """
        self.enemy = enemy

    def reset_battleground(self):
        """
        Resets battleground, nothing more
        """
        self.__init__()

    def start_game(self) -> None:
        """
        Starts game, adds hello message
        """
        Logger().add_message("The game has begun!")
        self.game_is_running = True

    def _check_players_hp(self) -> None:
        """
        Checks if player or enemy dead
        """
        if True in [self.player.check_player_is_dead, self.enemy.check_player_is_dead]:
            self.game_is_running = False

    def _regenerate_players_stamina(self) -> None:
        """
        Recovers players' stamina each turn
        """
        if self.game_is_running:
            self.player.recovery_stamina(self.stamina_recovery)
            self.enemy.recovery_stamina(self.stamina_recovery)

    def next_turn(self) -> None:
        """
        Check if some player dead
        If the game continues, regenerates stamina and uses enemy's abilities this turn
        """
        self._check_players_hp()
        if self.game_is_running:
            self._regenerate_players_stamina()
            self.enemy.use_attack(target=self.player)
        else:
            self.end_game()

    def skip_turn(self) -> None:
        """
        If you want to skip your turn in some reason
        """
        if self.game_is_running:
            Logger().add_message(f"{self.player.name} skipped his turn")
            self.next_turn()

    def player_attack(self) -> None:
        """
        Player uses 'use_attack' method
        """
        if self.game_is_running:
            self.player.use_attack(target=self.enemy)
            self.next_turn()

    def player_use_skill(self) -> None:
        """
        Player uses 'use_skill' method
        """
        if self.game_is_running:
            self.player.use_skill(target=self.enemy)
            self.next_turn()

    def end_game(self) -> None:
        """
        Game ends with some message
        """
        self.game_is_running = False

        if self.player.check_player_is_dead():
            Logger().add_message(f"{self.player.name} was defeated.")
        elif self.enemy.check_player_is_dead():
            Logger().add_message(f"{self.enemy.name} was defeated.")
        else:
            Logger().add_message("Draw")
