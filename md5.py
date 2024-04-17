import hashlib
from sys import argv

def md5hash(filename):
    md5_hash = hashlib.md5()
    with open(filename,"rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        return md5_hash.hexdigest()

print('here', argv[1])
print(md5hash(argv[1]))