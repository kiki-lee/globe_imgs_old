@namespace
class SpriteKind:
    NPC1 = SpriteKind.create()
    NPC2 = SpriteKind.create()
    NPC3 = SpriteKind.create()
    NPC4 = SpriteKind.create()
    Complete = SpriteKind.create()
    BUCKETS = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(10)
    sprites.destroy(projectile, effects.spray, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.BUCKETS, on_on_overlap)

def on_b_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        HG Basketball
    """), TNT, 100, 0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def Level_1_Trivia():
    global Current_Level, Wham, Hotshot, Torch, Coach_Sweet_Lou, DialogueMode
    Current_Level = 1
    if Current_Level == 1:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
        scene.set_background_image(assets.image("""
            myImage0
        """))
        scroller.scroll_background_with_camera(scroller.CameraScrollMode.BOTH_DIRECTIONS,
            scroller.BackgroundLayer.LAYER2)
    elif Current_Level == 2:
        scene.set_background_image(assets.image("""
            Basketball Court
        """))
        tiles.set_current_tilemap(tilemap("""
            level11
        """))
    else:
        game.game_over(False)
    Wham = sprites.create(assets.image("""
        Wham
    """), SpriteKind.NPC1)
    animation.run_image_animation(Wham, assets.animation("""
        Wham shooting
    """), 200, True)
    Wham.set_position(224, 72)
    Wham.say_text("Hi! I'm Wham!", 500, True)
    Hotshot = sprites.create(assets.image("""
        Hotshot
    """), SpriteKind.NPC2)
    animation.run_image_animation(Hotshot,
        assets.animation("""
            Hotshot dribbling
        """),
        200,
        True)
    Hotshot.set_position(448, 72)
    Hotshot.say_text("Hi! I'm Hotshot!", 500, False)
    Torch = sprites.create(assets.image("""
        Torch
    """), SpriteKind.NPC3)
    animation.run_image_animation(Torch,
        assets.animation("""
            Torch blocking
        """),
        200,
        True)
    Torch.set_position(672, 72)
    Coach_Sweet_Lou = sprites.create(assets.image("""
        Coach Sweet Lou
    """), SpriteKind.NPC4)
    Coach_Sweet_Lou.set_position(920, 72)
    Coach_Sweet_Lou.say_text("Hi! I'm Coach Sweet Lou!", 500, False)
    DialogueMode = False

def on_a_pressed():
    if TNT.vy == 0:
        TNT.vy = -150
        music.play(music.melody_playable(music.jump_up),
            music.PlaybackMode.UNTIL_DONE)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    animation.run_image_animation(TNT,
        assets.animation("""
            TNT  left dribble
        """),
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    global DialogueMode
    DialogueMode = True
    game.show_long_text("The Harlem Globetrotters played in Harlem, New York for the first time in what year?",
        DialogLayout.BOTTOM)
    story.show_player_choices("1968", "1926")
    if story.check_last_answer("1926"):
        info.change_score_by(-10)
    elif story.check_last_answer("1968"):
        info.change_score_by(25)
    DialogueMode = False
    Hotshot.set_kind(SpriteKind.Complete)
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC2, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    global DialogueMode
    DialogueMode = True
    game.show_long_text("In how many countries and territories have the Harlem Globetrotters performed in their history?",
        DialogLayout.BOTTOM)
    story.show_player_choices("124", "134")
    if story.check_last_answer("134"):
        info.change_score_by(-10)
    elif story.check_last_answer("124"):
        info.change_score_by(25)
    DialogueMode = False
    Coach_Sweet_Lou.set_kind(SpriteKind.Complete)
    sprites.destroy(Coach_Sweet_Lou)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC4, on_on_overlap3)

def on_right_pressed():
    animation.run_image_animation(TNT,
        assets.animation("""
            TNT walking-dribbling
        """),
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap4(sprite22, otherSprite22):
    global DialogueMode
    DialogueMode = True
    game.show_long_text("Who was the first woman to play for the Harlem Globetrotters?",
        DialogLayout.BOTTOM)
    story.show_player_choices("TNT Lister", "Lynette Woodard")
    if story.check_last_answer("TNT Lister"):
        info.change_score_by(-10)
    elif story.check_last_answer("Lynette Woodard"):
        info.change_score_by(25)
    DialogueMode = False
    Torch.set_kind(SpriteKind.Complete)
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC3, on_on_overlap4)

def Level_2_Basketball_Game():
    global Current_Level, BALL_1, Backboards
    Current_Level = 2
    TNT.say_text("Press B to shoot the basketballs. You must get to 300 points!",
        1000,
        False)
    tiles.set_current_tilemap(tilemap("""
        level11
    """))
    scene.set_background_image(assets.image("""
        Basketball Court
    """))
    BALL_1 = sprites.create(assets.image("""
            HG Basketball
        """),
        SpriteKind.projectile)
    Backboards = sprites.create(assets.image("""
        Backboards
    """), SpriteKind.BUCKETS)
    Backboards.set_position(140, 53)
    Backboards.set_stay_in_screen(True)

def on_on_score():
    game.show_long_text("You can now become a Harlem Globetrotter!!!",
        DialogLayout.FULL)
    game.set_game_over_effect(True, effects.confetti)
    game.game_over(True)
    music.play(music.melody_playable(music.magic_wand),
        music.PlaybackMode.UNTIL_DONE)
info.on_score(200, on_on_score)

def on_on_overlap5(sprite4, otherSprite4):
    global DialogueMode
    DialogueMode = True
    game.show_long_text("\"Who founded the Harlem Globetrotters?\"",
        DialogLayout.BOTTOM)
    story.show_player_choices("A) Barack Obama", "B) Abe Saperstein")
    if story.check_last_answer("A) Barack Obama"):
        info.change_score_by(-10)
    elif story.check_last_answer("B) Abe Saperstein"):
        info.change_score_by(25)
    DialogueMode = False
    Wham.set_kind(SpriteKind.Complete)
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.NPC1, on_on_overlap5)

Backboards: Sprite = None
BALL_1: Sprite = None
DialogueMode = False
Coach_Sweet_Lou: Sprite = None
Torch: Sprite = None
Hotshot: Sprite = None
Wham: Sprite = None
projectile: Sprite = None
Current_Level = 0
TNT: Sprite = None
TNT = sprites.create(assets.image("""
        TNT standing dribble
    """),
    SpriteKind.player)
animation.run_image_animation(TNT,
    assets.animation("""
        TNT walking-dribbling
    """),
    200,
    True)
game.show_long_text("Get a Harlem Globetrotter into the game and help them to score. Press A to begin.",
    DialogLayout.FULL)
TNT.ay = 275
controller.move_sprite(TNT, 100, 0)
TNT.say_text("Hi! I'm TNT!", 1000, False)
scene.camera_follow_sprite(TNT)
Current_Level = 0
Level_1_Trivia()

def on_on_update():
    global Current_Level
    if info.score() >= 100:
        Current_Level += 2
        Level_2_Basketball_Game()
    elif info.score() <= -10:
        game.show_long_text("TRY AGAIN!                You need 100 points to get to the basketball court.                    YOU GOT THIS!!!",
            DialogLayout.FULL)
        game.set_game_over_playable(False, music.melody_playable(music.ba_ding), True)
        game.reset()
game.on_update(on_on_update)

def on_forever():
    if DialogueMode == False:
        controller.move_sprite(TNT, 100, 0)
    elif DialogueMode == True:
        controller.move_sprite(TNT, 0, 0)
forever(on_forever)
