"""
Fun with Anagrams
Given an array of strings, remove each string that is an anagram of an earlier string, then return the remaining array in sorted order.

Example
str = ['code', 'doce', 'ecod', 'framer', 'frame']

code and doce are anagrams. Remove doce from the array and keep the first occurrence code in the array.
code and ecod are anagrams. Remove ecod from the array and keep the first occurrence code in the array.
code and framer are not anagrams. Keep both strings in the array.
framer and frame are not anagrams due to the extra r in framer. Keep both strings in the array.
Order the remaining strings in ascending order: ['code','frame','framer'].
"""
flag = True


def checkAnagram(orig, comp):
    output = False

    if len(orig) == len(comp):
        if sorted(orig) == sorted(comp):
            output = True

    return output


def funWithAnagrams(arr):
    # input arr = ['code', 'doce', 'ecod', 'framer', 'frame']
    # output cleaned arr = ['code', 'frame', 'framer']

    curr_elem = arr[0]
    queue = arr[1:]

    output = []
    output.append(curr_elem)

    while len(queue) > 0:
        next_elem = queue[0]

        if flag:
            print(f"\nentering the while loop")
            print(f"curr_elem = {curr_elem}")
            print(f"next_elem = {next_elem}")
            print(f"queue = {queue}")

        if curr_elem in output:
            if checkAnagram(curr_elem, next_elem):
                if flag:
                    print(f"they're anagrams")
                queue.pop(0)
            else:
                if flag:
                    print("they're NOT anagrams")

                output.append(next_elem)
                curr_elem = next_elem
                queue.pop(0)

    print(output)


arr = ["a", "b", "c", "d", "e"]
funWithAnagrams(arr)
