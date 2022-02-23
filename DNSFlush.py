import os
commands = ['sudo systemd-resolve --flush-caches', 'sudo systemctl restart systemd-resolved']
y = True
while (y == True):
    x = input('Press q to quit, s for statistics or f to flush')
    if (x == 'q'):
        y = False
    elif (x == 's'):
        os.system('sudo systemd-resolve --statistics')
    elif (x == 'f'):
        for command in commands:
            os.system(command)
        print('DNS has been flushed!')
    else:
        print('Invalid Option')
print('Come back soon!')
