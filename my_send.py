import sender
from sys import argv

if __name__ == '__main__':
    try:
        sender.send(argv[1])
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)