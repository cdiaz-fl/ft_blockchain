import datetime
from hashlib import sha256

class Block:
  def __init__(self, transactions, prev_hash):
    self.timestamp = datetime.datetime.now()
    self.transactions = transactions
    self.prev_hash = prev_hash
    self.hash = self.generate_hash()
    
  def print_block(self):
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    
  def generate_hash(self):
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.prev_hash)
    block_hash = sha256(block_contents.encode())
    return block_hash.hexdigest()
