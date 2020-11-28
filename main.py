
def decode_torrent(filename):
    with open(filename) as fp:
        data = fp.read()
    print(data)

def main():
    print("Welcome to Nel n Friends Torrent Client")
    link = input("please provide the link to your torrent: ")


if __name__ == '__main__':
    main()