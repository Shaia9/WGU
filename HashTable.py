#CREATE CHAINING HASHTABLE



class HashTable:
    def __init__(self, start_capacity=10):
        self.mapping = []
        for _ in range(start_capacity):
            self.mapping.append([])

        # Hash Key Creation
        def hash_key(self, key):
            return int(key) % len(self.mapping)

        # Insert into Hash Table
        def insert(self, key, value):
            insert_hash = self.hash_key(key)
            insert_value = [key, value]

            if self.mapping[insert_hash] == None:
                self.mapping[insert_hash] = list([insert_value])
                return True
            else:
                for pair in self.mapping[insert_hash]:
                    if pair[0] == key:
                        pair[1] = insert_value
                        return True
                self.mapping[insert_hash].append(insert_value)
                return True

        # Updating package in Hash Table
        def update(self, key, value):
           insert_hash = self.hash_key(key)
           if self.mapping(insert_hash) != None:
               for pair in self.mapping[insert_hash]:
                   if pair[0] == key:
                       pair[1] == value
                       print(pair[1])
                       return True
           else:
               print('Error updating key' + key)

        # Returning value from Hash Table
        def retrieve_value(self, key):
            insert_hash = self.hash_key(key)
            if self.mapping(insert_hash) is not None:
                for pair in self.mapping[insert_hash]:
                    if pair[0] == key:
                        return pair[1]
            return None

        # Removing value from Hash Table
        def remove(self, key):
            insert_hash = self.hash_key(key)
            if self.mapping(insert_hash) == None:
                return False
            for i in range(0, len(self.mapping[insert_hash])):
                if self.mapping[insert_hash][i][0] == key:
                    self.mapping[insert_hash].pop(i)
                    return True
                return False

    class EnterHashTable:
        def __init__(self, key, item):
            self.key = key
            self.item = item
