# this is From Tim 
# what is the birthday paradox?
# sharing common birthday is surprisingly likely

# collision are likely

import random
import hashlib

def our_hash_fun(random_key):
    # turn random key into a string so we can encode
    x = f"{random_key}".encode()
    # put bytes into sha256
    x = hashlib.sha256(x)
    # get out the hash (hexdigest)
    x = x.hexdigest()
    # turn back into base-10 number
    x = int(x, 16)
    return x


def how_many_before_collision(lst_len):
    # initialization
    all_indices = set()
    collision = False
    indices_made = 0
    while not collision:
        # create random number in (0, 1)
        random_key = random.random()
        hashed = our_hash_fun(random_key)
        new_index = hashed % lst_len

        if new_index in all_indices:
            # exit while loop if key already exist
            collision = True
        # otherwise track new index
        all_indices.add(new_index)
        indices_made += 1

    print(f"Hash before collision:, {indices_made}, buckets:{lst_len}, load factor: {indices_made/lst_len}")

how_many_before_collision(8)
