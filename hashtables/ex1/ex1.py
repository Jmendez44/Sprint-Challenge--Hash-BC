#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for i in length:
        if (hash_table_retrieve(ht, weights[i]) != -1):
            index_1 = i
            index_2 = hash_table_retrieve(ht, weights[i])
        else:
            hash_table_insert(ht, (limit - weights[i]))


    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
