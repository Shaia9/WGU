#CREATE CHAINING HASHTABLE



class HashTable:
    def __init__(self, start_capacity=10):
        self.map = []
        for _ in range(start_capacity):
            self.map.append([])

        # Hash Key Creation
        def hash_key(self, key):
            return int(key) % len(self.map)

        # Insert into Hash Table
        def insert(self, key, value):
            insert_hash = self.hash_key(key)
            insert_value = [key, value]

            if self.map[insert_hash] == None:
                self.map[insert_hash] = list([insert_value])
                return True
            else:
                for pair in self.map[insert_hash]:
                    if pair[0] == key:
                        pair[1] = insert_value
                        return True
                self.map[insert_hash].append(insert_value)
                return True

        # Updating package in Hash Table
        def update(self, key, value):
           insert_hash = self.hash_key(key)
           if self.map(insert_hash) != None:
               for pair in self.map[insert_hash]:
                   if pair[0] == key:
                       var = pair[1] == value
                       print(pair[1])
                       return True
           else:
               print('Error updating key' + key)

        # Returning value from Hash Table
        def retrieve_value(self, key):
            insert_hash = self.hash_key(key)
            if self.map(insert_hash) is not None:
                for pair in self.map[insert_hash]:
                    if pair[0] == key:
                        return pair[1]
            return None

        # Removing value from Hash Table
        def remove(self, key):
            insert_hash = self.hash_key(key)
            if self.map(insert_hash) == None:
                return False
            for i in range(0, len(self.map[insert_hash])):
                if self.map[insert_hash][i][0] == key:
                    self.map[insert_hash].pop(i)
                    return True
                return False

    class EnterHashTable:
        def __init__(self, key, item):
            self.key = key
            self.item = item
