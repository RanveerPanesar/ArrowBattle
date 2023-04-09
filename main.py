@namespace
class SpriteKind:
    Arrow = SpriteKind.create()

def on_player4_connected():
    scene.set_background_image(assets.image("""
        4pbg
    """))
    set_players(4)
controller.player4.on_event(ControllerEvent.CONNECTED, on_player4_connected)

def on_button_multiplayer_down_pressed(player2):
    mp.get_player_sprite(player2).set_image(assets.image("""
        3
    """))
    if arrow.image.equals(assets.image("""
        3
    """)):
        mp.change_player_state_by(player2, MultiplayerState.score, 1)
mp.on_button_event(mp.MultiplayerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_down_pressed)

def on_player3_connected():
    scene.set_background_image(assets.image("""
        3pbg
    """))
    set_players(3)
controller.player3.on_event(ControllerEvent.CONNECTED, on_player3_connected)

def on_button_multiplayer_left_pressed(player22):
    mp.get_player_sprite(player22).set_image(assets.image("""
        1
    """))
    if arrow.image.equals(assets.image("""
        1
    """)):
        mp.change_player_state_by(player22, MultiplayerState.score, 1)
mp.on_button_event(mp.MultiplayerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_left_pressed)

def on_button_multiplayer_up_pressed(player23):
    mp.get_player_sprite(player23).set_image(assets.image("""
        0
    """))
    if arrow.image.equals(assets.image("""
        0
    """)):
        mp.change_player_state_by(player23, MultiplayerState.score, 1)
mp.on_button_event(mp.MultiplayerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_up_pressed)

def set_players(num: number):
    sprites.destroy_all_sprites_of_kind(SpriteKind.player)
    index = 0
    while index <= num - 1:
        mp.set_player_sprite(mp.index_to_player(index),
            sprites.create(assets.image("""
                0
            """), SpriteKind.player))
        mp.get_player_sprite(mp.index_to_player(index)).change_scale(0.75, ScaleAnchor.MIDDLE)
        mp.get_player_sprite(mp.index_to_player(index)).set_position(80 / num * index + 80 / num * (index + 1), 90)
        index += 1

def on_button_multiplayer_right_pressed(player24):
    mp.get_player_sprite(player24).set_image(assets.image("""
        2
    """))
    if arrow.image.equals(assets.image("""
        2
    """)):
        mp.change_player_state_by(player24, MultiplayerState.score, 1)
mp.on_button_event(mp.MultiplayerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_right_pressed)

arrow: Sprite = None
scene.set_background_image(assets.image("""
    2pbg
"""))
arrow_list = [assets.image("""
        0
    """),
    assets.image("""
        1
    """),
    assets.image("""
        2
    """),
    assets.image("""
        3
    """)]
arrow = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.Arrow)
arrow.set_position(80, 30)
game.show_long_text("Follow and match the arrow sequence shown above by clicking the arrow keys.",
    DialogLayout.CENTER)
set_players(2)
carnival.start_countdown_game(71, carnival.WinTypes.MULTI)
music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
        4750,
        4783,
        255,
        0,
        449,
        SoundExpressionEffect.NONE,
        InterpolationCurve.CURVE),
    SoundExpressionPlayMode.IN_BACKGROUND)

def on_update_interval():
    arrow.set_image(arrow_list._pick_random())
game.on_update_interval(500, on_update_interval)
