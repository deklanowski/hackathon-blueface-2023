import arcade

from arcade_game.arcade_platformer.config.config import SCREEN_WIDTH, SCREEN_HEIGHT, ASSETS_PATH
from .cad_view import CadView
from .media_player import MediaPlayer


class ObjectiveView(arcade.View):
    """
    Displays a welcome screen and prompts the user to begin the game.

    Displays a background image, play a sounds and wait for pressing the Enter key to start the game.
    You do not have to modify these to complete the mandatory challenges.
    """

    def __init__(self, intro_media_player: MediaPlayer) -> None:
        super().__init__()

        self.start_view = None

        self.intro_media_player = intro_media_player

        self.game_view = None

        # Find the title image in the images folder
        second_image_path = ASSETS_PATH / "images" / "objective.png"

        # Load our title image
        self.second_image = arcade.load_texture(second_image_path)

        self.switch_screen_timer = 0.0
        # self.update_background_image(self.first_image)

    def on_draw(self) -> None:
        # Start the rendering loop
        arcade.start_render()

        # Draw a rectangle filled with our title image
        arcade.draw_texture_rectangle(
            center_x=SCREEN_WIDTH / 2,
            center_y=SCREEN_HEIGHT / 2,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            texture=self.second_image,
        )

    def on_update(self, delta_time: float) -> None:
        """Manages the timer to toggle the instructions

        Arguments:
            delta_time -- time passed since last update
        """
        self.switch_screen_timer += delta_time

        # If the timer has run out, we toggle the instructions
        if self.switch_screen_timer > 1:
            self.start_view = CadView(self.intro_media_player)
            self.window.show_view(self.start_view)
