import time , webbrowser 

# my original intro , X

#print('Hello and welcome! This is my first project on my own, thanks for joining :) ')
#print()
#time.sleep(2.5)
#print('My name is Kyler, I like nature, traveling, and computer science ')
#time.sleep(.02)
#print('   ------- ')
#time.sleep(.07)
#print('  |.-----.|')
#time.sleep(.04)
#print('  ||x . x||')
#time.sleep(.09)
#print('  ||_.-._||')
#time.sleep(.02)
#print('  `--)-(--`')
#time.sleep(.05)
#print('___[=== o]___')
#time.sleep(.07)
#print('|:::::::::::|/')
#time.sleep(.4)
#print('`-=========-`')


# typing effect function ->

def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05) # adjust the time delay here as needed

        # Intro
type_text("Hello, welcome to my first project, thank")
print()
type_text('My name is Kyler, I like nature, traveling, and computer science.')
print()
type_text('              .-------.         ')
print()
type_text( '.---------.   |  ===  |')
print()
type_text( '|.-"""""-.|   |  : :  |')
print()
type_text( '||   PC   |   | Gurgs |')
print()
type_text( '|-.....-. |   |:::::::|')
print()
type_text( '`\"\")---(")    |._____.|')
print()
type_text('/:::::::::::\" _"')
print()
type_text(':::=======:::/`/`/')
print()
type_text('`"""""""""""""`  -/')


print()
print()
print()
type_text('What is your name?')
print()
print()
name = str(input())
print()
time.sleep(.5)
print()
type_text(f'Hi {name} :D ')
print()
print()
type_text('I started coding for the first time about 14 months ago, I quickly gave up.')
print()
print()
type_text('I came back around to it, and it\'s been a blast.')
time.sleep(2.5)
print()
type_text('I\'m currently reading Automate the boring stuff. Learning the basic code has been tough, but it\'s been super rewarding.')
print()
time.sleep(1.5)
print()
type_text('Find me on LinkedIn :D')
print()
print()
time.sleep(.3)
type_text('https://www.linkedin.com/in/kylermcguire/')
print()
print()
time.sleep(1)
type_text(f'Ok, enough about me, let\'s begin {name}!')
print()
print()
print()

# print(Fore.RED + 'some red text') -  I want to ask for favorite color, change text to that color
states = {'Alabama':'',
          'Alaska':'',
          'Arizona':'',
          'Arkansas':'',
          'California':'',
          'Colorado':'',
          'Connecticut':'',
          'Delaware':'',
          'Florida':'',
          'Georgia':'',
          'Hawaii':'',
          'Idaho':'',
          'Illinois':'',
          'Indiana':'',
          'Iowa':'',
          'Kansas':'',
          'Kentucky':'',
          'Louisiana':'',
          'Maine':'',
          'Maryland':'',
          'Massachusetts':'',
          'Michigan':'',
          'Minnesota':'',
          'Mississippi':'',
          'Missouri':'',
          'Montana':'',
          'Nebraska':'',
          'Nevada':'',
          'New Hampshire':'',
          'New Jersey':'',
          'New Mexico':'',
          'New York':'',
          'North Carolina':'',
          'Ohio':'Is this ron?',
          'Oklahoma':'',
          'Oregon':'',
          'Pennysylvania':'',
          'Rhode Island':'',
          'South Carolina':'',
          'South Dakota':'',
          'Tennessee':'',
          'Texas':'',
          'Utah':'',
          'Vermont':'',
          'Virginia':'',
          'Washington':'',
          'West Virginia':'',
          'Wisconsin':'',
          'Wyoming':''}
#while True:
print('What state are you from?')
print()
in_usa = input()
   # if in_states == '':
     #   break
    #if in_states in states:
        #print(states[in_states] + ' is the Birthday of ' + name)
    # else:
    #    print('i do not have bday info for '+ name)
     #   print('what is their bday?')
       # bday = input()
      #  birthdays[name] = bday
        #print('birthday database updated')
         
if in_usa in states:
          if in_usa in states:
            print('Checking database....')
            time.sleep(5)
            print(f'This is what we have for {in_usa}')
            print()
            type_text(states[in_usa])
           
else: # will add state
    type_text('I do not have info for that location')
    print()
    type_text(f'Can you tell me something about {in_usa}?')
    print()
    new_location = input()
    print()
    states[in_usa] = new_location
    type_text(' Database updating..')
    print()
    type_text('10%..')
    print()
    time.sleep(1.5)
    type_text('45%..')
    print()
    time.sleep(1.5)
    type_text('70%..')
    print()
    time.sleep(1.5)
    type_text('99%.....')
    print()
    time.sleep(5)
    type_text('Database update complete!')
print()
type_text('Would you like to see the database contents?')
print()
verify_user = input()
print('Please select:|Y|-|N|')
verify_input = input()

if verify_input == 'Y':
    print(f'Welcome to the database {name} ')
    print('__________________________________')
    print()
    print()
    print(states.keys())
    print()
    print()
    print('__________________________________')

 # print(states.items())
#type_text('Are you located in the States? Yes or No')
#where_at = input()
#if where_at == 'yes' or where_at == 'Yes':
 #   type_text('what state are you in?')
  #  in_usa = input()
   # type_text(f'Awesome! Here are some fun facts about {in_usa}! : ')
#if_usa in states:
 #   type_text[states].value()
#elif where_at == 'no' or where_at == 'No':
 #   type_text('Where are you located?')
  #  not_in_usa = input()
   # type_text(f'Nice, I\'m not sure if I know of {not_in_usa}')
