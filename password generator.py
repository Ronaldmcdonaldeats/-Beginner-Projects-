import random
import string

length = int(input("How long should the password be?"))

character = (string.ascii_letters + string.digits + string.punctuation)

password = ''.join(random.choice(character) for _ in range(length))

print ("Your password is: ", password)