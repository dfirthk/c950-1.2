
#Hash Table class and it's associated functions
class HashTable:
    def __init__(self, capacity=41):
        self.table = []
        for i in range(capacity):
            self.table.append([])

    def __repr__(self):
        return repr(self.table)

    #Insert function for new items and to also update existing
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucketList = self.table[bucket]
        for value in bucketList:
            if value[0] == key:
                value[1] = item
                return True
        keyValue = [key, item]
        bucketList.append(keyValue)
        return True

    #Search function to look through the hash for matching key
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucketList = self.table[bucket]
        for value in bucketList:
            if value[0] == key:
                return value[1]
        return None

    #Delete function for items with matching key
    def delete(self, key):
        bucket = hash(key) % len(self.table)
        bucketList = self.table[bucket]
        if key in bucketList:
            bucketList.remove(key)