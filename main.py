import sys
import argparse
import server
import client


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--send', action='store_true', help="To Send File")
    parser.add_argument('-r', '--receive', action='store_true', help="To Receive File")
    parser.add_argument('filename')
    args = parser.parse_args()
    if args.filename and args.send:
        server.File_Server(args.filename)
        print("DONE")
    elif args.receive:
        client.File_Client()
        print("RECEIVED")
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == '__main__':
    main()
