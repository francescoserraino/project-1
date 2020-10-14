import pyglet

def play_sound(soundfile): 
    sound = pyglet.media.load(soundfile)
    sound.play()

def gif_player(animated_gif):
#Takes and plays inserted gif 
    animation = pyglet.image.load_animation(animated_gif)
    animSprite = pyglet.sprite.Sprite(animation)


    w = animSprite.width
    h = animSprite.height

    window = pyglet.window.Window(width=w, height=h)

    r,g,b,alpha = 0.5,0.5,0.8,0.5


    pyglet.gl.glClearColor(r,g,b,alpha)

    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()

    pyglet.app.run()

gif_player(r'../gifs/check_bed')