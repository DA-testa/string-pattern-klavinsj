# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    # this is the sample return, notice the rstrip function
    izvele = input()
    if "F" in izvele:
        fails = input()
        fails = "./tests/" + fails
        ievade = open(fails,"r").readlines()
        return (ievade[0].rstrip(), ievade[1].rstrip())
    if "I" in izvele:
        return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    result = []
    d = 256
    num = 101

    P = len(pattern)
    T = len(text)

    x = 0
    l = 0
    h = 1

    for i in range(P - 1):
        h = (h * d) % num

    for i in range(P):
        x = (d * x + ord(pattern[i])) % num
        l = (d * l + ord(text[i])) % num

    for i in range(T - P + 1):
        if x == l:
            for j in range(P):
                if text[i + j] != pattern[j]:
                    break
                else:
                    j += 1
            if j == P:
                result.append(i)
        if i < T - P:
            l = (d * (l - ord(text[i])*h) + ord(text[i+P])) % num
            if l < 0:
                l = l + num
                
    # and return an iterable variable
    return result
    # and return an iterable variable

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

