#Write all additional functions here
#testing git
import pyglet
import speech_recognition as sr

def speech(question):
    r = sr.Recognizer()    
    with sr.Microphone() as source:
        print(question)
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text


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
        
    def close(event):
        window.close()

    pyglet.clock.schedule_once(close, 5.0)
        
    pyglet.app.run()

# define rooms and items
door_a = {
    "name": "door a",
    "type": "door",
    "open_gif": './gifs/open_door_1.gif',
    "locked_gif": './gifs/cant_open_door.gif',
    "open_sound": './sounds/closedoor.wav',
    "locked_sound": './sounds/aww.wav',
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
    "gif": './gifs/find_key.gif',
}

door_b = {
    "name": "door b",
    "type": "door",
    "open_gif": './gifs/open_door_aggresive.gif',
    'locked_gif': './gifs/cant_open_door_2.gif',
    "open_sound": './sounds/closedoor.wav',
    "locked_sound": './sounds/aww.wav',
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
    "gif": './gifs/find_key.gif',
}


door_c = {
    "name": "door c",
    "type": "door",
    "open_gif": './gifs/storm_through_door.gif',
    "locked_gif": './gifs/cant_open_door.gif',
    "open_sound": './sounds/closedoor.wav',
    "locked_sound": './sounds/aww.wav',
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
    "gif": './gifs/find_key.gif',
}

door_d = {
    "name": "door d",
    "type": "door",
    "open_gif": './gifs/exit_house.gif',
    'locked_gif': './gifs/cant_open_door_2.gif',
    "open_sound": './sounds/closedoor.wav',
    "locked_sound": './sounds/aww.wav',
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
    "gif": './gifs/find_key.gif',
}

couch = {
    "name": "couch",
    "type": "furniture",
    'gif': './gifs/looking_at_couch.gif',
    "sound": "./sounds/boring.wav",
}

piano = {
    "name": "piano",
    "type": "furniture",
    "gif": "./gifs/creepy_piano.gif",
    "sound": "./sounds/piano.wav",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
    'gif': './gifs/check_bed.gif',
    "sound": "./sounds/bedspring.wav",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
    'gif': './gifs/dresser_gif.gif',
    "sound": "./sounds/dresser.wav",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
    'gif': './gifs/check_bed.gif',
    "sound": "./sounds/snoring.wav",
}

dining_table = {
    "name": "dining table",
    "type": "furniture",
    'gif': './gifs/check_table.gif',
    "sound": "./sounds/glassbreak.wav",
}


game_room = {
    "name": "game room",
    "type": "room",
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
} 

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
} 

living_room = {
    "name": "living room",
    "type": "room",
} 

outside = {
  "name": "outside"
}

all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "bedroom 1": [queen_bed, door_c, door_b, door_a],
    "bedroom 2": [double_bed, dresser, door_b],
    "living room": [dining_table, door_d, door_c],
    "piano": [key_a],
    "queen bed": [key_b],
    "dresser": [key_d],
    "double bed": [key_c],
    "outside": [door_d],
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1,bedroom_2],
    "door c": [bedroom_1, living_room],
    "door d": [living_room, outside]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!")
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore', 'examine' or 'speech' for speech recognition?").strip()
        # sr
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        elif intended_action == "speech":
            result = speech("Say examine or explore")
            #print(result)
            if result == 'examine':
                examine_item(input("What would you like to examine?").strip())
            elif result == 'explore' or 'explorer':
                explore_room(room)
                play_room(room)
            else:
                print("Not sure what you mean. Type 'explore' or 'examine'.")
                play_room(room)
            linebreak()
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
                    play_sound(item["locked_sound"])
                    gif_player(item["locked_gif"])
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                    play_sound(item["sound"])
                    gif_player(item["gif"])
                else:
                    output += "There isn't anything interesting about it."
                    play_sound(item["sound"])
                    gif_player(item["gif"])
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    result = ''
    result2 = ''
    if next_room:        
        result = input("Do you want to go to the next room? Type 'yes', 'no' or 'speech' for speech recognition")
        if result == 'yes':
            play_sound(item["open_sound"])
            gif_player(item["open_gif"])
            play_room(next_room)
        elif result == 'speech':
            try:
                result2 = speech("Do you want to go to the next room? Say 'yes', 'no'")
                if result2 == 'yes':
                    play_sound(item["open_sound"])
                    gif_player(item["open_gif"])
                    play_room(next_room)
                elif result2 == 'no':
                    play_room(current_room)
                else:
                    print(f"You said {result2},this is not an option, you are back in {current_room['name']}")
                    play_room(current_room)
            except:
                print(f"We did not understand what you said, you are back in {current_room['name']}")
                play_room(current_room) 
                
        else:
            play_room(current_room)       
    else:
        play_room(current_room)   

game_state = INIT_GAME_STATE.copy()

start_game()
