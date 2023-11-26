import arcade

from arcade_game.arcade_platformer.config.config import PLAYER_START_X, PLAYER_START_Y, ASSETS_PATH, \
    PLAYER_MOVE_SPEED, PLAYER_JUMP_SPEED


class Player:
    """
    Controls the player animations (images for the various positions) and movements
    """

    def __init__(self):
        self.movement_timer = None
        self.player = self.create_player_sprite()
        self.physics_engine = None
        self.jump_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / "abirdjump.wav")
        )

    def set_physics_engine(self, physics_engine: arcade.PhysicsEnginePlatformer):
        self.physics_engine = physics_engine

    @staticmethod
    def create_player_sprite() -> arcade.AnimatedWalkingSprite:
        """Creates the animated player sprite

        Returns:
            The properly set up player sprite
        """
        # Where are the player images stored?
        texture_path = ASSETS_PATH / "images" / "player"

        # Set up the appropriate textures
        walking_paths = [
            texture_path / f"timrun{x}.png" for x in (1, 2, 3)
        ]
        jump_paths = [
            texture_path / f"PC Computer - Braid - Tim climb{x}.png" for x in (1, 2, 3, 4)
        ]
        climbing_paths = [
            texture_path / f"PC Computer - Braid - Tim climb{x}.png" for x in (1, 2, 3, 4)
        ]
        standing_path = [
            texture_path / f"PC Computer - Braid - Tim stand{x}.png" for x in (1, 2, 3, 4, 5, 6, 7)
        ]
        attack_path = [
            texture_path / f"PC Computer - Braid - Tim phone{x}-overlay.png" for x in (1, 2, 3)
        ]
        # Load them all now
        walking_right_textures = [
            arcade.load_texture(texture) for texture in walking_paths
        ]
        walking_left_textures = [
            arcade.load_texture(texture, mirrored=True)
            for texture in walking_paths
        ]

        walking_up_textures = [
            arcade.load_texture(texture) for texture in climbing_paths
        ]
        walking_down_textures = [
            arcade.load_texture(texture) for texture in climbing_paths
        ]

        standing_right_textures = [
            arcade.load_texture(texture) for texture in standing_path
        ]

        standing_left_textures = [
            arcade.load_texture(texture, mirrored=True)
            for texture in standing_path
        ]

        attack_right_textures = [
            arcade.load_texture(texture) for texture in attack_path
        ]

        attack_left_textures = [
            arcade.load_texture(texture, mirrored=True)
            for texture in attack_path
        ]

        # Create the sprite
        player = arcade.AnimatedWalkingSprite()

        # Add the proper textures
        player.stand_left_textures = standing_left_textures
        player.stand_right_textures = standing_right_textures
        player.walk_left_textures = walking_left_textures
        player.walk_right_textures = walking_right_textures
        player.walk_up_textures = walking_up_textures
        player.walk_down_textures = walking_down_textures
        player.attack_left_textures = attack_left_textures
        player.attack_right_textures = attack_right_textures

        # Set the player defaults
        player.center_x = PLAYER_START_X
        player.center_y = PLAYER_START_Y
        player.state = arcade.FACE_RIGHT

        # Set the initial texture
        player.texture = player.stand_right_textures[0]

        return player

    def move_left(self):
        self.player.change_x = -PLAYER_MOVE_SPEED

    def move_right(self):
        self.player.change_x = PLAYER_MOVE_SPEED

    def nudge_right(self, nudge_seconds=2):
        """Move right for nudge_seconds then stop"""
        self.move_right()
        self.movement_timer = arcade.schedule(self.reset_movement, nudge_seconds)

    def nudge_left(self, nudge_seconds=2):
        """Move left for nudge_seconds then stop"""
        self.move_left()
        self.movement_timer = arcade.schedule(self.reset_movement, nudge_seconds)

    def move_up(self):
        # Check if player can climb up or down
        if self.physics_engine.is_on_ladder():
            self.player.change_x = 0  # have to stop before climbing
            self.player.change_y = PLAYER_MOVE_SPEED

    def move_down(self):
        if self.physics_engine.is_on_ladder():
            self.player.change_x = 0
            self.player.change_y = -PLAYER_MOVE_SPEED

    def stop(self):
        """Stop horizontal motion"""
        self.player.change_x = 0

    def hold(self):
        """Stop upward motion"""
        self.player.change_y = 0

    def jump(self):
        if self.physics_engine.can_jump():
            self.physics_engine.jump(PLAYER_JUMP_SPEED)
            # Play the jump sound
            arcade.play_sound(self.jump_sound)

    def jump_right(self, jump_speed=PLAYER_JUMP_SPEED, move_speed=PLAYER_MOVE_SPEED):
        """Allows player to jump up and move right when on platform or ladder"""
        if self.physics_engine.can_jump() or self.physics_engine.is_on_ladder():
            self.physics_engine.jump(jump_speed)
            self.player.change_x = move_speed
            # Play the jump sound
            arcade.play_sound(self.jump_sound)

    def jump_left(self):
        """Allows player to jump up and move left when on platform or ladder"""
        if self.physics_engine.can_jump() or self.physics_engine.is_on_ladder():
            self.physics_engine.jump(PLAYER_JUMP_SPEED)
            self.player.change_x = -PLAYER_MOVE_SPEED
            # Play the jump sound
            arcade.play_sound(self.jump_sound)

    def jump_right_timed(self, interval_seconds=2, jump_speed=PLAYER_JUMP_SPEED, move_speed=PLAYER_MOVE_SPEED):
        """Allows player to 'jump_right' for a specified interval then stop dead"""
        self.jump_right(jump_speed=jump_speed, move_speed=move_speed)
        self.movement_timer = arcade.schedule(self.reset_movement, interval_seconds)

    def jump_right_turbo(self, jump_speed=PLAYER_JUMP_SPEED + 2, move_speed=PLAYER_MOVE_SPEED + 3):
        """Help us get over the wide water jump on level 4"""
        self.jump_right_timed(jump_speed=jump_speed, move_speed=move_speed)

    def jump_left_timed(self, interval_seconds=2):
        """Allows player to 'jump_left' for a specified interval then stop dead"""
        self.jump_left()
        self.movement_timer = arcade.schedule(self.reset_movement, interval_seconds)

    def reset_movement(self, delta_time):
        """
        This function is called from the scheduler to stop player movement. It is used in the
        timed movement functions, e.g. jump_right_timed.
        """
        self.player.change_x = 0
        self.player.change_y = 0
        arcade.unschedule(self.reset_movement)
        self.movement_timer = None


