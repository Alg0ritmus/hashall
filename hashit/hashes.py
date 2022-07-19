import hashlib

class Hash:
    def __init__(self) -> None:
        self.digest = None
    
    def sha3_224(self,data):
        hasher = hashlib.sha3_224()
        hasher.update(data)
        self.digest = hasher.digest()
    
    def sha3_256(self,data):
        hasher = hashlib.sha3_256()
        hasher.update(data)
        self.digest = hasher.digest()


    def sha3_384(self,data):
        hasher = hashlib.sha3_384()
        hasher.update(data)
        self.digest = hasher.digest()

    def sha3_512(self,data):
        hasher = hashlib.sha3_512()
        hasher.update(data)
        self.digest = hasher.digest()

    def hashTest(self,arg,data):
        temp=0
        switch={
            "sha3_224": self.sha3_224,
            "sha3_256": self.sha3_256,
            "sha3_384": self.sha3_384,
            "sha3_512": self.sha3_512
        }
        switch[arg](data)
    
    def getDigest(self):
        return self.digest

    def getHexDigest(self):
        return self.digest.hex()