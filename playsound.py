import pyglet
def play_sound_furniture(soundfile): 
    sound = pyglet.media.load(soundfile)
    sound.play()

play_sound_furniture('airplane-landing_daniel_simion.wav')