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

    # Adding all weights to hash table
    for index in range(0, length):
        hash_table_insert(ht, weights[index], index)
        print('ht', ht)
    # Check if limit - weights[index] is True, if so we found the solution
    for index in range(0, length):
        print('pre', hash_table_retrieve(ht, limit - weights[index]))


    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
