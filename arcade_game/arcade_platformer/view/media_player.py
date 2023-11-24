import arcade

from arcade_game.arcade_platformer.config.config import ASSETS_PATH


class MediaPlayer:

    def __init__(self, media_filename):
        self.media_player = None
        self.media = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / media_filename)
        )
        self.playing = False

    def play(self, volume=0.3, loop=False):
        self.media_player = self.media.play(volume=volume, loop=loop)
        self.playing = True

    def stop(self):
        self.media.stop(self.media_player)
        self.playing = False
