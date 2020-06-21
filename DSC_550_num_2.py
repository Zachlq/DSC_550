# Zach Quinn
# DSC 550 
# 21 June 2020
# Program function: Determine if an item is derivable or non-derivable.
# Program description: Creates, iterates and replaces item sets in existing dictionaries to determine if subsets are derivable.

import collections
import sys


# Please note, this is not the full, functional code base. 
# I was close to getting Charm to work, but without Charm, I could not crack derivable item sets.
# Therefore, I will utilize in-line comments to walk through how this should work, not how it does.

# Checks if item is a subset of a string value.
# All_characters_in_string("ABCDE", "AC") -> True
def is_subset_string(full_string, part):
     found_all = True
     for item in part:
          if item not in full_string:
               found_all = False
               break
     return found_all

# Replace_key
# Example: item AE replace_key 'B', replace_value = {1, 2, 3, 4, 5}
def search_and_replace(P, look_for={}, add_on=""):
     save = {}
     for p_key, p_value in P.items():
          if p_key == look_for:
               save[p_key] = p_value

# Examine all items 'AE' in 'ADEC' -> True
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
    f = open('/Users/zachquinn/Desktop/DSC_500/itemsets.txt', 'r')
    # Reads second file 
    f_2 = open('/Users/zachquinn/Desktop/DSC_500/hdi.txt', 'r')
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

    # Given my difficulty with Charm, I was unable to get the next steps to work. 
    # However, as I understand it, here are the steps to conceive and execute this function:
    # 1) Define and deploy a similar brute force read function to read file, strip white space and split strings.
    # 2) Initialize a search and replace function to search dictionaries for similar entries and new keys to the dictionary.
    # 3) Create blank dictionaries for new item sets. 
    # 4) Use conditional logic to employ properties of Charm to determine relationships among tids/items. I.e. 'A U C', 'A | C', etc.
    # 5) If item exists in dictionary, add new key to existing dictionary.
    # 6) If not, search and replace, delete or recursively iterate over repeated item set.
    # 7) Iterate over the new closed item set.
    # 8) For each new item set, generate possible subsets and check to see if they exist within the closed set. I.e. 'ABEC'