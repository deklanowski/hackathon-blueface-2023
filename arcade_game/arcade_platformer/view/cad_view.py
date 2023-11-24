import arcade

from arcade_game.arcade_platformer.config.config import SCREEN_WIDTH, SCREEN_HEIGHT, ASSETS_PATH
from arcade_game.arcade_platformer.player.player import Player

from .platform_view import PlatformerView
from .media_player import MediaPlayer


class CadView(arcade.View):
    """
    Displays a welcome screen and prompts the user to begin the game.

    Displays a background image, play a sounds and wait for pressing the Enter key to start the game.
    You do not have to modify these to complete the mandatory challenges.
    """ 
    def __init__(self, player: Player, intro_player: MediaPlayer) -> None:
        super().__init__()

        self.player = player

        self.intro_player = intro_player

        self.game_view = None

        # Find the title image in the images folder
        second_image_path = ASSETS_PATH / "images" / "CAD.png"

        # Load our title image
        self.second_image = arcade.load_texture(second_image_path)
        
        self.switch_screen_timer = 0.0
        # self.update_background_image(self.first_image)
        self.show_instructions = True

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
        if self.show_instructions:
            arcade.draw_text(
                "Press enter to Start the game",
                start_x=250,
                start_y=170,
                color=arcade.color.SELECTIVE_YELLOW,
                font_size=30,
            )

    def on_key_press(self, key: int, modifiers: int) -> None:
        """Start the game when the user presses the enter key

        Arguments:
            key -- Which key was pressed
            modifiers -- What modifiers were active
        """
        if key == arcade.key.RETURN:
            # Stop intro music
            self.intro_player.stop()

            # Launch Game view
            self.game_view = PlatformerView(self.player)
            self.game_view.setup()
            self.window.show_view(self.game_view)
    
    