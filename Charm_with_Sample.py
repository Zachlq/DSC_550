# Zach Quinn
# DSC 550
# 21 June 2020
# File function: Finds minimum support of closed frequent item set 
# File description: A combination of ordered and empty dictionary functions that loop over closed frequent item sets.
import collections
import sys

# checks if part is a subset of full_String
# for instance all_characters_in_string("ABCDE", "AC") -> True
def is_subset_string(full_string, part):
     found_all = True
     for item in part:
          if item not in full_string:
               found_all = False
               break
     return found_all

# replace_key
# example: item AE replace_key 'B', replace_value = {1, 2, 3, 4, 5}
def search_and_replace(P, look_for={}, add_on=""):
     save = {}
     for p_key, p_value in P.items():
          if p_key == look_for:
               save[p_key] = p_value

          # examine all items 'AE' in 'ADEC' -> True
          # "AF" in "ADEC" -> False
          if is_subset_string(p_key, look_for):
               save[p_key] = p_value

     for saved_key, saved_value in save.items():
          if add_on in saved_key:
               continue
          del P[saved_key]
          P["{}{}".format(saved_key,add_on)] = saved_value

     return P

def create_dict_from_file(filename):
    """ Read in a file of itemsets
        each row is considered the transaction id
        and each line contains the items associated
        with it.
        This function returns a dictionary that
        has a key set as the tid and has values
        of the list of items (strings)
    """
    # Reads file
    f = open(filename, 'r')
    # Defines blank dictionary
    d = {}
    # Iterates for transaction id, line items and initializes counter (enumerate) function.
    for tids, line_items in enumerate(f):
        # Creates a dictionary with a key of d and a value of 'tids.'
        # Strips white space and splits strings into individual letters.
        d[tids+1] = [j.rstrip() for j in line_items.split(' ')
                   if j != '\n']
    # Defines blank dictionary 'p.'
    p = {}
    # Iterates for the key and value in dictionary d with key items.
    for key, value in d.items():
        # Iterates for item in value.
        for item in value:
            # Conditional logic: if item exists in the newly formed p dictionary, adds a new key to the dictionary.
            if item in p:
                p[item].add(key)
            # Else: If item does not exist, store a key.
            else:
                p[item] = {key}
    # Collections/ordered dict function specifies how to store items in output list.
    P = collections.OrderedDict(sorted(p.items(), key=lambda t: len(t[1])))
    return P

def charm_logic(transaction_set_i, key_i, key_j, transaction_set_j, P, minsup):
    p = {}
    # Create a new variable that stores the intersection of transaction set i and transaction set j.
    transaction_set_i_j = transaction_set_i & transaction_set_j
    # If the length of transaction set i, j is greater than minsup and...
    if len(transaction_set_i_j) >= minsup:
        # if the diference of j and i does not meet min sup
        if not transaction_set_i.difference(transaction_set_j) and not transaction_set_j.difference(transaction_set_i):
            # On first pass, replace tid_i with the union of i and j in the dictionary 'p.'
            p[key_i] = transaction_set_i | transaction_set_j
            # On second pass, replace tid_i with the union of i and j in dictionary 'P.'
            P[key_i] = transaction_set_i | transaction_set_j
            # For tid j, the dictionary of 'p' will be empty.
            #p[key_j] ==
            del P[key_j]
        # Subset logic set:
        elif transaction_set_i.issubset(transaction_set_j):
            search_and_replace(p, look_for=key_i, add_on= key_j)
            search_and_replace(P, look_for=key_i, add_on= key_j)
        else:
            p[key_i + key_j] = transaction_set_i | transaction_set_j
    # Do nothing with the current iteration.
    return P, p


def charm(P, minsup, c):
    # Stack: Ordered list. Iterate over p_stack.
    P_stack = [k for k, val in P.items()]
    # p is a dictionary where the key is the item and the value is the list of transactions where that item occurs.
    i = 0
    # We look through key of i and tid of i in the dictionary p.items.
    for key_i in P_stack:
        transaction_set_i = P[key_i]
        # Establish initial value for j.
        j = 0
        p = {}
        for key_j in P_stack:
            # And if j is a greater value than i...
            if j > i:
                transaction_set_j = P[key_j]
                # Print the key of j, the key of i, the transaction set of j and the transaction set of i.
                print(key_i, key_j, transaction_set_i, transaction_set_j)
                P, p = charm_logic(transaction_set_i, key_i, key_j, transaction_set_j, P, minsup)
            j = j + 1
            if len(p) != 0:
                charm(p, minsup, c)
        # Specify that we add one to i.
        i = i + 1
        # if ∃Z∈C, such that Xi⊆Z and t(Xi)=t(Z) then
        #   C=C∪Xi //Add Xi to closedset
        found = False
        for item in c:
            if is_subset_string(item, key_i):
                # TODO Calculate support for item and confirm that support(item) == support(key_i)
                found = True
        if not found:
            c.add(key_i)



P = create_dict_from_file(filename="/Users/zachquinn/Desktop/DSC_500/Sample.txt")#TODO sys.argv[1])
result = set()
#TODO minsup = sys.argv[2]
minsup = 3
print(charm(P, minsup, result))
print(result)