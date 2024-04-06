from sys import argv
from yeelight_extras import Bulb, Group, flows, scenes

def main():
    # CHECK 1: Is argument passed correctly?
    if len(argv) != 2:
        raise Exception('Arguments passed incorrectly. Please call in the form "python launcher.py <name_of_flow>".')

    g1 = Bulb('gameroom-light-1') 
    g2 = Bulb('gameroom-light-2')
    g3 = Bulb('gameroom-light-3')
    g4 = Bulb('gameroom-light-4')
    g = Group([g1, g2, g3, g4])
    g.turn_on()

    # CHECK 2: Are all bulbs in group online?
    try:
        g.get_properties()
    except:
        raise Exception('Bulb connection failed. Likely Bulb or Group is offline.')

    # SCRIPT: If both checks passed, command group to run flow or scene.
    floworscene = argv[1]
    if floworscene in dir(scenes):
        g.set_scene(floworscene)
    elif floworscene in dir(flows):
        g.set_flow(floworscene)
    else:
        raise Exception(f'There is no Flow or Scene named {floworscene}.')

if __name__ == '__main__':
    main()
