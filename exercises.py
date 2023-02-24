#Question 1

from IPython.display import clear_output

address_book2 = {}

for key, value in adress_book.items():
    key = input('Who are you entering into the address book?')
    while key != 'quit':
        return address_book2[0]
        value = input(f"What is {key}'s address?")
        while value != 'quit':
            return address_book2[1]
            ask = input(f"Would you like to enter another name? y/n)")
            if ask != 'y':
                break
                  
#????? I got stuck on this one





#Question 2

s1 = {'09:00', '10:30', '11:30', '12:00', '13:00', '14:30'}
s2 = {'09:30', '10:00', '10:30', '12:00', '14:30', '16:00'}
s3 = {'09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00'}
s4 = {'11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00'}

s5 = s1.intersection(s2)
print(s5)

s6 = s5.intersection(s3)
print(s6)

s7 = s6.intersection(s4)
print(s7)

print(f"Times that work for everybody: {s7}")