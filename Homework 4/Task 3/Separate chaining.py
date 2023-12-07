def hash_key(key, size):
    return hash(key) % size

def insert(hash_table, key, value):
    index = hash_key(key, len(hash_table))
    for i, (k, v) in enumerate(hash_table[index]):
        if k == key:
            hash_table[index][i] = (key, value)
            break
    else:
        hash_table[index].append((key, value))

def get(hash_table, key):
    index = hash_key(key, len(hash_table))
    for k, v in hash_table[index]:
        if k == key:
            return v
        return None

def remove(hash_table, key):
    index = hash_key(key, len(hash_table))
    for i, (k, v) in enumerate(hash_table[index]):
        if k == key:
            del hash_table[index][i]
            break

size = 10

hash_table = [[] for _ in range(size)] #Loob tühja hajustabeli, mis on list listidest.
insert(hash_table, "key1", "value1")
insert(hash_table, "key2", "value2")
print(get(hash_table, "key1")) #Tagastab väärtuse.
remove(hash_table, "key1")
print(get(hash_table, "key1")) #Tagastab NONE!