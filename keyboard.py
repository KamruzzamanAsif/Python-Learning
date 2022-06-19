key_string = "`1234567890-=qwertyuiop[]asdfghjkl;'\zxcvbnm,./"

shift  = input()
string = input()

if(shift == "R"):
    for j in range(len(string)):
        for i in range(len(key_string)):
            if(string[j] == key_string[i]):
                print(key_string[i-1], end="")
else:
    for j in range(len(string)):
        for i in range(len(key_string)):
            if(string[j] == key_string[i]):
                print(key_string[i+1], end="")
                
                