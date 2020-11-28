import bencode

'''
Core Features
1. Communicate with the tracker (with support for compact format)
2. Download a file from other instances of your client
3. Download a file from official BitTorrent clients

Extra Credit
If you successfully implement the core features of this project, you may optionally implement one
or more features below for extra credit:
1. Implement support for UDP-tracker protocol.
2. Implement optimistic unchoking (see \Choking and Optimistic Unchoking" in [1]).
3. Implement the rarest-rst strategy (see \Piece Downloading Strategy" in [1]).
4. Implement an endgame mode (see \End Game" in [1]).
5. Implement an optional BitTyrant mode (see [2]).
6. Implement PropShare [4] and design experiments to compare performance to the ocial client.
'''

def decode_torrent(filename):
    with open(filename, 'rb') as fdata:
        data = fdata.read()
    decoded = bencode.decode(data)
    for a in decoded:
        print(a)
        print(decoded[a])

def main():
    print("Welcome to Nel n Friends Torrent Client")
    link = input("please provide the link to your torrent: ")
    decode_torrent("./torrent_files/big-buck-bunny.torrent")


if __name__ == '__main__':
    main()