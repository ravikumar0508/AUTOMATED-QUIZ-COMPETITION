#!/usr/bin/env python
# coding: utf-8

# In[1]:


user_name =input("please enter your name")
print("welcome to quiz game world and questions are asked from python :",user_name)
start_quiz =(input("are you ready?(yes or no):"))


def new_game():
    guesses =[]
    correct_guesses =0
    question_num =1
    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
            
        guess =input("enter(a,b,c, or d):") 
        guess =guess.lower()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
        
    display_score(correct_guesses,guesses)    
        
    
        
            
            
            
def check_answer(answer,guess):
    if answer == guess:
        print("correcr answer")
        return 1
    else:
        print("Wrong answer")
        return 0
    
    
    
    
    
    
def display_score(correct_guesses,guesses):
    print("------------------------")
    print("RESULTS")
    print("------------------------")
    print("answers:", end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("guesses:", end=" ")
    for i in guesses:
        print(i,end=" ")
    print()
    
    score = int((correct_guesses/len(questions))*100)
    print("your score is :"+str(score)+"%")
    
    

def play_again():
    play = input("do you want to play the game again?(yes or no):")
    play = play.lower()
    if play =="yes":
        return True
    else:
        return False
    
    
    
    
    
questions ={"What is a correct syntax to output 'Hello World' in Python?":"c","How do you insert COMMENTS in Python code?":"b","Which one is NOT a legal variable name?":"a","How do you create a variable with the numeric value 5?":"b","What is the correct file extension for Python files?":"b","How do you create a variable with the floating number 2.8?":"b","What is the correct syntax to output the type of a variable or object in Python?":"c","What is the correct way to create a function in Python?":"b","What is a correct syntax to return the first character in a string?":"a","Which method can be used to remove any whitespace from both the beginning and the end of a string?":"c","Which method can be used to return a string in upper case letters?":"c","Which method can be used to replace parts of a string?":"b","Which operator is used to multiply numbers?":"b","Which operator can be used to compare two values?":"b","Which of these collections defines a LIST?":"b"}
options =[["a.print()","b.none","c.print('Hello World')"],["a.@","b.#","c.&","d.%"],["a.my-var","b.none","c.MyVar"],["a.x =5","b.both are correct","c.x=int(5)"],["a.PP","b.py","c.python"],["a.x=2.8","b.both are correct","c.x=float(2.8)"],["a.none","b,type","c.print(type(x))"],["a.function","b.def function(x)","c.create function"],["a.index[o]","b.1","c.first"],["a.remove","b.del","c.strip()"],["a.caps","b.bold","c.upper()"],["a.alter","b.replace()","c.swap()"],["a.multi","b.*","c.x"],["a.compare","b.==","c.="],["a.{1,2,3}","b.[1,2,3]","c.(1,2,3)"]]


new_game()

while play_again():
    new_game()
    
print("thanks for playing the quiz game MR/MRS: ",user_name)


# In[32]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




