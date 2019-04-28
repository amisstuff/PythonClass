names = [ 'kaila', 'david', 'jonathan', 'wendy' ]

#prints out each person's name by placement in list
print (names[0])
print (names[1])
print (names[2])
print (names[3])

message = ("I am learning python with " + names[0].title())
print (message)
message = ("I am learning python with " + names[1].title())
print (message)
message = ("I am learning python with " + names[2].title())
print (message)
message = ("I am learning python with " + names[3].title())
print (message)

transit = [ 'car', 'plane', 'ship', 'bart' ]
print ("I need to " + transit[-1] + " to the airport to catch the " + transit[1])
print ("this " + transit[0] + " is so slow compared to the " + transit[-1])

print ("\n****************************")

#append() adds another element to the list
          #ex: motorcycles.append('honda')
#insert() adds it to a specific position in the list
          #ex: motorcycles.insert(0, 'ducati')
#del removes an item from the list by position in the list
          #ex: del motorcycles[0]
#pop() removes the last item on the list but lets you work with it (use it) after removing it.
          #ex: popped_motorcycle = motorcycles.pop()
#remove() removes the elememts by specific name (value) if you don't know the position in the list
          #ex: motorcycles.remove('ducati') 
        
print ("\n****************************")        

party_ppl = [ 'tony', 'steve', 'nat' ]

message = ("Come to my party " + party_ppl[0].title() + "!")
print (message)
message = ("Come to my party " + party_ppl[1].title() + "!")
print (message)
message = ("Come to my party " + party_ppl[2].title() + "!")
print (message)

print ("\n****************************")
popped_party_ppl = party_ppl.pop()
print (popped_party_ppl.title() + " couln't make it!!")
party_ppl.append('thor')
print (party_ppl)
print ("\n****************************")
message = ("Come to my party " + party_ppl[0].title() + "!")
print (message)
message = ("Come to my party " + party_ppl[1].title() + "!")
print (message)
message = ("Come to my party " + party_ppl[2].title() + "!")
print (message)

print ("\n****************************")

print ("We found a bigger table!")
party_ppl.insert(0, 'deadpool')
party_ppl.insert(2, 'hawkeye')
party_ppl.append('antman')
message = ("Come to my party " + party_ppl[0].title() + "!")
print (message)
message = ("Come to my party " + party_ppl[1].title() + "!")
print (message)
message = ("Come to my party " + party_ppl[2].title() + "!")
print (message)
message = ("Come to my party " + party_ppl[3].title() + "!")
print (message)
message = ("Come to my party " + party_ppl[4].title() + "!")
print (message)
message = ("Come to my party " + party_ppl[5].title() + "!")
print (message)

print ("\n****************************")
print ("I can only invite two people!")
popped_party_ppl = party_ppl.pop()
print (popped_party_ppl.title() + " has been uninvited!")
print (party_ppl)
popped_party_ppl = party_ppl.pop()
print (popped_party_ppl.title() + " has been uninvited!")
print (party_ppl)
popped_party_ppl = party_ppl.pop()
print (popped_party_ppl.title() + " has been uninvited!")
print (party_ppl)
popped_party_ppl = party_ppl.pop()
print (popped_party_ppl.title() + " has been uninvited!")
print (party_ppl)

print ("\n****************************")

print (party_ppl[0] + " is still invited!")
print (party_ppl[1] + " is still invited!")

del party_ppl[0]
del party_ppl[1]
print (party_ppl)
