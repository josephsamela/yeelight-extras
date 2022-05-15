from sys import argv
from yeelight_extras import Bulb, Group

def main():
    # CHECK 1: Is argument passed correctly?
    if len(argv) != 2:
        raise Exception('Arguments passed incorrectly. Please call in the form "python launcher.py <name_of_flow>".')

    g1 = Bulb('gameroom1') 
    g2 = Bulb('gameroom2')
    g3 = Bulb('gameroom3')
    g4 = Bulb('gameroom4')
    g = Group([g1, g2, g3, g4])

    # CHECK 2: Are all bulbs in group online?
    try:
        g.get_properties()
    except:
        raise Exception('Bulb connection failed. Likely Bulb or Group is offline.')

    # SCRIPT: If both checks passed, command group to run flow.
    flow = argv[1]
    print(f'Running flow: {flow}')
    g.set_flow(flow)

if __name__ == '__main__':
    main()
