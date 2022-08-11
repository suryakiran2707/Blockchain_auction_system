import datetime
import hashlib


class createBlock:
    # nonce is the value we are adding in the block for block difficulty
    def __init__(self, prevblockhash , data, timestamp, nonce, name):
        self.prevblockhash = prevblockhash
        self.data = data
        self.timestamp = timestamp
        self.nonce = nonce
        self.name = name
        self.hash = self.calhash()

    def __str__(self):
        return "Block details are as follows : previous block hash is % s, data present in block is % s , time stamp is %s, nonce value is %s, block hash is %s" % (self.prevblockhash, self.data,str(self.timestamp),self.nonce,self.hash)

    def calhash(self):
        return hashlib.sha256(
            (self.prevblockhash + "-" + self.data + "-" + str(self.timestamp) + "-" + str(self.nonce)).encode()).hexdigest()



