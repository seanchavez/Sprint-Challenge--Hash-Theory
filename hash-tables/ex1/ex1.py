def get_indices_of_item_weights(weights, limit):
    weight_table = {}
    for i in range(len(weights)):
        if weights[i] not in weight_table:
            weight_table[weights[i]] = i
        if limit - weights[i] in weight_table and weight_table[limit - weights[i]] != i:
            return (i, weight_table[limit - weights[i]])
    return ()
if __name__ == '__main__':
  # You can write code here to test your implementation using the Python repl
  pass 