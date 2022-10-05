
#%%
i = 0

while i <= 1:
    print ("food")
    i = i + 1 

food = ["fries, burger, hotdog, salad"]
print (len(food))


beatles = [
    "John",
    "Paul",
    "George",
    "Ringo"]

print (len(beatles))

# %%

numbers = [0, 3, -12, 99]

mixed_values = [1, True, 0.4, "yay"]

# %%

def print_list (list):
    index = 0 
    while index < len(list):
        print (list[index])
        index = index + 1
    
elements = ["Jamil", "Juan", "Chin", "Alexia"]
print_list(elements)

#%%

def print_list(list):
    index = 0
    while index <= len(list) - 1:
        print(list[index])
        index = index + 1
        
print_list ([4,3,2,1])


# %%

ramones = ["Jhonny", "Joey", "Markee", "Dee-Dee"]

philippes = ["Philippe", "pepe"]

print (ramones + philippes)

# %%

beatles = [
    "John",
    "Paul",
    "George",
    "Ringo"
]

beatles[3] = "Pepe"
print (beatles)

# %%

coding_club = []
coding_club.append ("Jamil")
coding_club.append ("Philippe")


print (coding_club)

coding_club.pop (0)


# %%

