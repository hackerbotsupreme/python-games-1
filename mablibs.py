# string concatenation (aka how to put strings together )
# suppose we want to create a string that says 'subscribe to _____'
# some string variable 

# a few ways to do this 
# print( 'subscribe to '+youtuber)# by adding a plus sign 
# print('subcribe to {}'.format(youtuber))# format method 
# print(f'subscribe to {youtuber}')# using f string method 
# print('subscribe to ',youtuber)# using , / comma 
# let's go and see if there is any errors or not . 
# output 
#Desktop/games/mablibs.py
#subscribe to code with aloke  
#subcribe to code with aloke  
#subscribe to code with aloke  
#subscribe to  code with aloke  


# so lets talk about madlips
"""
Very Beginner Python Project by Kylie Ying
Madlibs using string concatenation
YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""
# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "subscribe to _____ "
# youtuber = "Kylie Ying" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
# output

# Adjective: amazing 
# Verb: skydive 
# Verb: jump
# Famous person: captain america 
# Computer programming is so amazing ! It makes me so excited all the time because I love to skydive . Stay hydrated and jump like you are captain america !