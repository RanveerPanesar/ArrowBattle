namespace SpriteKind {
    export const Arrow = SpriteKind.create()
}

controller.player4.onEvent(ControllerEvent.Connected, function on_player4_connected() {
    scene.setBackgroundImage(assets.image`
        4pbg
    `)
    set_players(4)
})
mp.onButtonEvent(mp.MultiplayerButton.Down, ControllerButtonEvent.Pressed, function on_button_multiplayer_down_pressed(player2: number) {
    mp.getPlayerSprite(player2).setImage(assets.image`
        3
    `)
    if (arrow.image.equals(assets.image`
        3
    `)) {
        mp.changePlayerStateBy(player2, MultiplayerState.Score, 1)
    }
    
})
controller.player3.onEvent(ControllerEvent.Connected, function on_player3_connected() {
    scene.setBackgroundImage(assets.image`
        3pbg
    `)
    set_players(3)
})
mp.onButtonEvent(mp.MultiplayerButton.Left, ControllerButtonEvent.Pressed, function on_button_multiplayer_left_pressed(player22: number) {
    mp.getPlayerSprite(player22).setImage(assets.image`
        1
    `)
    if (arrow.image.equals(assets.image`
        1
    `)) {
        mp.changePlayerStateBy(player22, MultiplayerState.Score, 1)
    }
    
})
mp.onButtonEvent(mp.MultiplayerButton.Up, ControllerButtonEvent.Pressed, function on_button_multiplayer_up_pressed(player23: number) {
    mp.getPlayerSprite(player23).setImage(assets.image`
        0
    `)
    if (arrow.image.equals(assets.image`
        0
    `)) {
        mp.changePlayerStateBy(player23, MultiplayerState.Score, 1)
    }
    
})
function set_players(num: number) {
    sprites.destroyAllSpritesOfKind(SpriteKind.Player)
    let index = 0
    while (index <= num - 1) {
        mp.setPlayerSprite(mp.indexToPlayer(index), sprites.create(assets.image`
                0
            `, SpriteKind.Player))
        mp.getPlayerSprite(mp.indexToPlayer(index)).changeScale(0.75, ScaleAnchor.Middle)
        mp.getPlayerSprite(mp.indexToPlayer(index)).setPosition(80 / num * index + 80 / num * (index + 1), 90)
        index += 1
    }
}

mp.onButtonEvent(mp.MultiplayerButton.Right, ControllerButtonEvent.Pressed, function on_button_multiplayer_right_pressed(player24: number) {
    mp.getPlayerSprite(player24).setImage(assets.image`
        2
    `)
    if (arrow.image.equals(assets.image`
        2
    `)) {
        mp.changePlayerStateBy(player24, MultiplayerState.Score, 1)
    }
    
})
let arrow : Sprite = null
scene.setBackgroundImage(assets.image`
    2pbg
`)
let arrow_list = [assets.image`
        0
    `, assets.image`
        1
    `, assets.image`
        2
    `, assets.image`
        3
    `]
arrow = sprites.create(img`
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
    `, SpriteKind.Arrow)
arrow.setPosition(80, 30)
game.showLongText("Follow and match the arrow sequence shown above by clicking the arrow keys.", DialogLayout.Center)
set_players(2)
carnival.startCountdownGame(71, carnival.WinTypes.Multi)
music.playSoundEffect(music.createSoundEffect(WaveShape.Triangle, 4750, 4783, 255, 0, 449, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.InBackground)
game.onUpdateInterval(500, function on_update_interval() {
    arrow.setImage(arrow_list._pickRandom())
})
