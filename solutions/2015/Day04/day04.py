""" 
Adds incrementing positive numbers to a given string until it matches an MD5 encoded 
hex digest starting in the given number of zeroes.
"""
import hashlib

def check_for_zeroes(hex_hash, target, found):
    return True if hex_hash[:target] == "0" * target else False

def main():
  string = input("Enter prefix string: ")
  target_num = int(input("Enter number of zeros to match on: "))

  found = False
  num = 1
  while not found:
    # turn the number into a string and concat onto the input
    string_to_hash = string + str(num)
    h_string = hashlib.md5(string_to_hash.encode())
    found = check_for_zeroes(h_string.hexdigest(), target_num, found)
    if found:
      print(f"First match: {num}")
    else:
      num +=1

if __name__ == "__main__":
  main()