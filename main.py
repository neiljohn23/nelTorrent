import bencode
#You are not allowed to make use of third-party libraries 
# except for a bencoder/bdecoder library of your choosing.

class Torrent:
        # init method or constructor    
    def __init__(self, filename=None):   
        if filename != None:
            self.tor_dict = self.decode_torrent(filename) 
            self.piece_len = self.tor_dict['info']['piece length']
            print("piece len is " + str(self.piece_len))
            print("num pieces is " + str(int(len(self.tor_dict['info']['pieces'])/20)))
    # Sample Method  
    # returns name of torrent (suggested) or path  
    def get_name(self):   
        return self.tor_dict['info']['name']   

    # decodes a bencoded file
    # returns a bencoded ordered dictionary of key value tuples
    def decode_torrent(self, filename):
        with open(filename, 'rb') as fdata:
            data = fdata.read()
        decoded = bencode.decode(data)
        return decoded

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

# torrent file spec
'''
metainfo files
Metainfo files (also known as .torrent files) are bencoded dictionaries with the following keys:

announce
The URL of the tracker.
info
This maps to a dictionary, with keys described below.
All strings in a .torrent file that contains text must be UTF-8 encoded.

info dictionary
The name key maps to a UTF-8 encoded string which is the suggested name to save the file (or directory) as. It is purely advisory.

piece length maps to the number of bytes in each piece the file is split into. For the purposes of transfer, files are split into fixed-size pieces which are all the same length except for possibly the last one which may be truncated. piece length is almost always a power of two, most commonly 2 18 = 256 K (BitTorrent prior to version 3.2 uses 2 20 = 1 M as default).

pieces maps to a string whose length is a multiple of 20. It is to be subdivided into strings of length 20, each of which is the SHA1 hash of the piece at the corresponding index.

There is also a key length or a key files, but not both or neither. If length is present then the download represents a single file, otherwise it represents a set of files which go in a directory structure.

In the single file case, length maps to the length of the file in bytes.

For the purposes of the other keys, the multi-file case is treated as only having a single file by concatenating the files in the order they appear in the files list. The files list is the value files maps to, and is a list of dictionaries containing the following keys:

length - The length of the file, in bytes.

path - A list of UTF-8 encoded strings corresponding to subdirectory names, the last of which is the actual file name (a zero length list is an error case).

In the single file case, the name key is the name of a file, in the muliple file case, it's the name of a directory.

'''



def main():
    print("Welcome to Nel n Friends Torrent Client")
    link = input("please provide the link to your torrent: ")
    t = Torrent(filename="./torrent_files/big-buck-bunny.torrent")
    print("ur torrent name is " + t.get_name())
    # print out the key,val parts of the dictionary
    for key in t.tor_dict:
        print(key + ": " + str(t.tor_dict[key]))


if __name__ == '__main__':
    main()