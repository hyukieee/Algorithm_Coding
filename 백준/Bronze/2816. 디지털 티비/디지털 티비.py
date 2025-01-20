N = int(input())
channels = [input().strip() for _ in range(N)]

commands = []
selection = 0

def press_button(cmd):
    global channels, selection
    commands.append(cmd)
    if cmd == '1':
        if selection < len(channels) - 1:
            selection += 1
    elif cmd == '2':
        if selection > 0:
            selection -= 1
    elif cmd == '3':
        if selection < len(channels) - 1:
            channels[selection], channels[selection + 1] = channels[selection + 1], channels[selection]
            selection += 1
    elif cmd == '4':
        if selection > 0:
            channels[selection], channels[selection - 1] = channels[selection - 1], channels[selection]
            selection -= 1

def move_channel(target, desired_pos):
    global selection
    while True:
        try:
            current_pos = channels.index(target)
        except ValueError:
            break
        if current_pos == desired_pos:
            break
        while selection < current_pos:
            press_button('1')
        while selection > current_pos:
            press_button('2')
        if current_pos > desired_pos:
            press_button('4')
        else:
            press_button('3')

move_channel("KBS1", 0)
move_channel("KBS2", 1)

print(''.join(commands))
