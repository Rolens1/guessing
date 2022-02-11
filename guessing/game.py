import random

def play() :
    playing = True if input('Do you want to play : y/n ') == 'y' else False

    if playing :

        min = 0
        diff = ''

        print('Choose your level of difficulty \n Very Easy - Unlimited Tries : 1 '
        '\n Easy - 5 tries              : 2'
        '\n Medium - 5 tries            : 3'
        '\n Hard - 8 tries              : 4'
        '\n Very Hard - 9 tries         : 5 ')

        while True:
            try:
                difficulty = input('Choose a valid Option ') 
                if difficulty == '1':
                    diff = 'very easy'
                    max = 10
                    tries = 10
                    break
                elif difficulty == '2':
                    diff = 'easy'
                    max = 10
                    tries = 5
                    break
                elif difficulty == '3':
                    diff = 'medium'
                    max = 100
                    tries = 5
                    break
                elif difficulty == '4':
                    diff = 'hard'
                    max = 500
                    tries = 8
                    break
                elif difficulty == '5':
                    diff = 'very hard'
                    max = 1000
                    tries = 9
                    break
            except ValueError:
                print('Choose a valid option : ')

        compChoice = random.randint(min,max)
        print(f'Difficulty set to {diff}, choose a number between {min} and {max}')
        print(f'You have {tries} tries left. Good luck!')

        while True:
            try :
                userChoice = int(input(f'Choose a number between {min} and {max}. {tries} tries Left: '))

                if userChoice > compChoice:
                    max = userChoice
                elif userChoice < compChoice:
                    min = userChoice
                elif userChoice == compChoice:
                    print("Well played")
                    playing = False
                    break
                
                tries -= 1

            except ValueError:
                print('Please write a valid option: ')
 
            if tries < 1 :
                    print(f'No luck, the answer was {compChoice}!')
                    playing = False
                    break
        
        play()



play()
print('Quitting game')
