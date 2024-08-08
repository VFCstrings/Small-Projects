from replit import clear

#HINT: You can call clear() to clear the output in the console.

print('Welcome to the secret auction program.')

not_more_bidders=False
list_bidders={}
while not not_more_bidders:
  
  name=input('What is your name?: ')
  bid=int(input('What is your bid?: '))
  
  list_bidders[name]=bid

  other_bidders=input('Are there any other bidders? Type "yes" or "no". ')
  if other_bidders=='yes':
    clear() 
  else:
    not_more_bidders=True
    max_key = max(list_bidders, key=list_bidders.get)
    max_value = list_bidders[max_key]
    print(f'The winner of the action is {max_key} with a bid of {max_value}$')
 
  