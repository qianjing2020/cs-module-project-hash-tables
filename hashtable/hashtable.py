class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` slots that accepts string keys
    """
    def __init__(self, capacity):
        # capacity need to be greater than assigned min
        if MIN_CAPACITY > capacity:
            print('Mininum capacity not comply')
        else: 
            self.capacity = capacity
            self.slots = [[] for i in range(capacity)]

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash table data. 
        (aka, the number of slots being used.) 
        """
        # number of used slots = capacity - the empty entry
        # empty_counts = 0
        # for slot in self.slots:
        #     if slot == []:
        #         empty_counts += 1
        # return self.capacity - empty_counts
        
        return self.capacity

    def get_load_factor(self):
        """
        Return load factor, the number of keys stored in the hash table divided by the capacity
        """
        # add all key occurence in all non-empty slots
        # initilizae 
        num_keys = 0
        for slot in self.slots:
            if slot ==[]:
                break
            # count number of elements in the linked list
            curr = slot
            while curr:
                num_keys += 1
                curr = curr.next
            
        load_factor = num_keys/self.capacity
        return load_factor

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """
        FNV_offset_basis = 14695981039346656037 
        FNV_prime = 1099511628211
        hash = FNV_offset_basis
        for b in key:
            hash = hash * FNV_prime
            # bitwise XOR
            hash = b ^ hash 
        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        """
        # hash the key
        hash = self.hash_index(key)
        # store value in slot
        # empty slot, directly store it          
        if self.slots[hash] == []:  
            self.slots[hash] = HashTableEntry(key, value)
        else:
            # slot not empty, go over linked list
            curr = self.slots[hash]
            # search for replicate key, overwrite if found, insert if not found
            while curr is not None:
                if curr.key == key:
                    # overwrite
                    curr.value = value
                    return
                curr = curr.next

            # else no replicate key, insert key value to head of linked list
            temp = self.slots[hash]
            self.slots[hash] = HashTableEntry(key, value)
            self.slots[hash].next = temp

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        """
        # hash key to find hash index
        hash = self.hash_index(key)
        # go to the slot, define first lin as current
        s = self.slots[hash]
        # if the correspondent slot is empty    
        if s.key == [] or s is None:
            print('Key is not found! Nothing deleted.')
            return 

        # if the first element in the slot match the key
        # put the next in the slot
        if s.key == key:
            self.slots[hash] = s.next
        
        # else loop through all the links search for the key until the end
        prev = s
        curr = s.next         
        while curr is not None:
            if curr.key == key:
                prev.next = curr.next 
            prev = curr
            curr = curr.next
        
      

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        # hash the key, go to the slot
        hash = self.hash_index(key)
        curr = self.slots[hash]

        # loop through the linked list in the slot if hash entry is not empty
        while curr != [] and curr is not None:        
            if curr.key ==  key:
                return curr.value
            curr = curr.next 
        
        # if empty or not key found
        return None
    
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """
        # temperarily hold the old array
        temp = self.slots
        
        # augument capacity
        self.slots = [[] for i in range(new_capacity)]        
        self.capacity = new_capacity
        
        # transfer old to new
        for slot in temp:
            # rehash 
            s = slot
            while s != [] and s is not None:
                key = s.key
                hash  = self.hash_index(key)        
                self.slots[hash] = HashTableEntry(s.key, s.value)
                s = s.next    

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print('---------'*3)
    print(f"Load factor is {ht.get_load_factor()}")
    
    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()
    new_capacity = ht.capacity

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    
    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    print('---------'*3)
    print(f"Load factor is {ht.get_load_factor()}")
