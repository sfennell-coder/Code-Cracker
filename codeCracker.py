# get password
print("Alert: this program can only crack codes that contains letters and numbers!")
file = open("/Users/Scottfennell/Desktop/Python/password.txt", 'r')
data = file.read()
# determine how many characters in password
d_l = len(data)
num_char = str(d_l)
print("Number of characters in password is " + num_char)

# random characters to get password

char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'J', 'K',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'l', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char_list = char

code = str(data)
target_password = code
password_length = d_l
status = 'ongoing'

def crack():
    import random
    global target_password, status, password_length
    count = 0
    print("Processing...")
    while status == "ongoing":
        guess = ""
        while len(guess) < password_length:
            while len(guess) < password_length:
                guess += random.choice(char_list)
            if guess == target_password:
                print("Password is: " + str(guess))
                status = "finished"
                count += 1
                print(str(count) + " guesses")
            else:
                print(guess)
                count += 1
while target_password != "":
    status = "ongoing"
    crack()
    print("_______")
    break