#CREATE CHAINING HASHTABLE



class HashTable:
    def __init__(self, start_capacity=40):
# Initialize the hash table w/ empty lists
        self.map = [[] for _ in range(start_capacity)]

    # Create Hash Key
    def hash_key(self, key):
        return int(key) % len(self.map)

    # Insert into Hash Table
    def insert(self, key, value):
        insert_hash = self.hash_key(key)
        insert_value = [key, value]

        # Check if key exists, update if it does
        for pair in self.map[insert_hash]:
            if pair[0] == key:
                # Update if exists
                pair[1] = value

                return True

        # If key doesn't exist append
        self.map[insert_hash].append(insert_value)
        return True

    # Update package in Hash Table
    def update(self, key, value):
        insert_hash = self.hash_key(key)
        for pair in self.map[insert_hash]:
            if pair[0] == key:
                # Update
                pair[1] = value

                return True
        # Key not Found
        return False

    # Retrieve value from Hash Table
    def retrieve_value(self, key):
        insert_hash = self.hash_key(key)
        for pair in self.map[insert_hash]:
            if pair[0] == key:
                # Return if key = found
                return pair[1]
        # Key not found
        return None

    # Logic to remove value
    def remove(self, key):
        insert_hash = self.hash_key(key)
        for i, pair in enumerate(self.map[insert_hash]):
            if pair[0] == key:
        # Remove key pair
                self.map[insert_hash].pop(i)
            return True
        # Key not found
        return False