dict_pairs = {"(": ")", "[": "]", "{": "}"}


def isEven(arr):
    output = False

    if ((len(arr)) % 2) == 0:
        output = True

    return output


def isOpen(char):
    output = False

    if char in dict_pairs.keys():
        output = True

    return output


def isMatch(c1, c2):
    output = False

    if dict_pairs[c1] == c2:
        output = True

    return output


def isValid(s: str) -> bool:
    output = False

    arr = []
    for char in s:
        arr.append(char)

    if isEven(arr):
        curr_elem = arr[0]
        queue = arr[1:]

        still_pending = []

        if isOpen(curr_elem):
            while len(queue) > 0:
                next_elem = queue[0]
                queue.pop(0)

                if isMatch(curr_elem, next_elem):
                    if len(still_pending) > 0:
                        curr_elem = still_pending[-1]
                        still_pending.pop(-1)
                else:
                    still_pending.append(curr_elem)
                    curr_elem = next_elem

            if len(still_pending) > 0:
                output = False
            else:
                output = True

    return output


arr = "()()[(()](())"
if isValid(arr):
    print("yess")
else:
    print("nope")

## missing some edge cases
# need to implement a stack


""" 
      # checking if the first elem is a closer
        if(self.isOpen(curr_elem)):

            while(len(queue)>0):

                next_elem = queue[0] # "["
                queue.pop(0)

                if(isOpen(curr_elem)):
                    if(isMatch(curr_elem,next_elem)):
                        curr_elem = next_elem
                    else:
                        stil_open.append(curr_elem)
                        
                        """
