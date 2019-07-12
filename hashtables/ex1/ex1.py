#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Adding all weights to hash table
    for index in range(0, length):
        hash_table_insert(ht, weights[index], index)
        # print('ht', ht)

    for i in range(length):
        print('ht', ht)
        # print('i' ,i)
        item = limit - weights[i] # 21 - 6 = 15
        answer = hash_table_retrieve(ht, item) #grabs 15 key returns index 3
        print(answer)
        if answer:
            return (answer, i)

    return None

# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))

def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")