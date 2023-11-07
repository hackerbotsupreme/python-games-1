# steps 
# a dictionary that stores queations and answers 
# and what we need to do once we have the dictionary 
# have a variable that tracks the score of the player 
# loop /iterate through the dictionary  uaing the key, value pairs 
#  display each question to the useer and alloe them to answer till they are right or wrong 
# show the final result when quiz is completed 

quiz={
    'Question1' :{
        'question':'what is the capital of the france?',  # dont forget the comma or else it will give you an error 
        'answer': 'paris '
    },
    'Question2':{
        'question':'what is the capital of the germany?',  # dont forget the comma or else it will give you an error 
        'answer': 'berlin'
    },
    'Question3':{
        'question':'what is the capital of the india?',  # dont forget the comma or else it will give you an error 
        'answer': 'new delhi'
    },
    'Question4':{
        'question':'what is the capital of the Italy?',  # dont forget the comma or else it will give you an error 
        'answer': 'rome '
    },
    'Question5':{
        'question':'what is the capital of the louda ?',  # dont forget the comma or else it will give you an error 
        'answer': 'madrid'
    },
    'Question6':{
        'question':'what is the capital of the spain?',  # dont forget the comma or else it will give you an error 
        'answer': 'portugal'
    },
    'Question7':{
        'question':'what is the capital of the Swetzerland  ?',  # dont forget the comma or else it will give you an error 
        'answer': 'thai'
    }
} 

score=0# to track the score of the user 

for key,value in quiz.items():
    print(value['question'])
    answer=input('answer?')

    if answer.lower()==value['answer'].lower():
        print('Correct')
        score= score+1 
        print('your score is :'+str(score))

    else:
        print('wrong ')
        print('the answer is :'+value['answer'])
        print('your score is :'+str(score ))
        print('')
        print('')

print('you got'+str(score)+'out of 7 ')
print('your percentage is' + str(score/7*100)+'%')

# output before adding space  
# what is the capital of the france?
##answer?paris
#wrong
#the answer is :paris
#your score is :0
#what is the capital of the germany?
#answer?berlin
#Correct
#your score is :1
#what is the capital of the india?
#answer?newdelhi
#wrong
#the answer is :new delhi
#your score is :1
#what is the capital of the Italy?
#answer?rome 
#Correct
#your score is :2
#what is the capital of the louda ?
#answer?madrid  
#wrong
#the answer is :madrid
#your score is :2
#what is the capital of the spain?
#answer?portugal 
#wrong
#the answer is :portugal
#your score is :2
#what is the capital of the Swetzerland  ?
##answer?thai
#Correct
#your score is :3




# output after adding space  # notice the spaces 
#hat is the capital of the france?
#answer?paris 
#Correct
#your score is :1
#what is the capital of the germany?
#answer?berlin
#Correct
#your score is :2
#what is the capital of the india?
#answer?newdelhi
#wrong 
#the answer is :new delhi
#your score is :2


#what is the capital of the Italy?
#answer?paris
#wrong
#the answer is :rome
#your score is :2


#what is the capital of the louda ?
#answer?berlin
#wrong
#the answer is :madrid
#your score is :2


#what is the capital of the spain?
#answer?dsdkj
#wrong
#the answer is :portugal
#your score is :2


#what is the capital of the Swetzerland  ?
#answer?ksfjh
#wrong
#he answer is :thai#
#your score is :2


#you got2out of 7
#your percentage is28.57142857142857%
#PS C:\Users\rekha\OneDrive\Desktop\games> 
