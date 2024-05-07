'''
    Game:
        - welcome message
        - options ----> exit
        - user choice ---> run game
        - ask play again
        - n ---> exit game


            options :
                -input list ----> 2list - even number
                                        - odd number
                - sentense ---> no duplicate , redundent =?
                - input number ---> 0 : number
                - unput 2 number -->
                - input 2 number --> all number // 2 number  0:100 
'''
class Game:
    def __init__(self):
        print('''welcome
Games:

    1 - Split Even And Odd Number
    2 - Remove Duplicates Game
    3 - Range Number
    4 - Numbers Divisible
    5 - Numbers Divisible 2
    6 - Exit 
    ''')

        user_choice = int(input('Enter Game Number : '))
        if user_choice == 1:
            input_lst = input('Enter list : ')
            lst = [int(number) for number in input_lst.split()]
            self.split_even_odd_number(lst)
        elif user_choice == 2:
            sentence = input('Enter sentence : ')
            self.sentence_duplicate_remover(sentence)
        elif user_choice == 3:
            end = int(input('Enter end number'))
            self.range_0_number(end)
        elif user_choice == 4:
            num1 = int(input('Enter frist Number : '))
            num2 = int(input('Enter second Number : '))
            self.print_numbers_divisible(num1,num2)  
        elif user_choice == 5:
            number1 = int(input('Enter frist Number : '))
            number2 = int(input('Enter second Number : '))
            self.print_numbers_divisible_2(number1,number2)

        elif user_choice == 6:
            print("Goodbye...!")
            return
        else:
            print('The Number Error')
            print('*****************')
            print()
            self.__init__()

        play_again = input('Enter ( Again ) to play again , ( Exit ) to exit ')
        if play_again == 'Again':
           self.__init__() 
        elif play_again == 'Exit':
            print("Goodbye...!")
            return
        else:
            print('The Number Error')
            print('*****************')
            self.play_again

    def split_even_odd_number(self, lst):
        even_numbers = []
        odd_numbers = []
        
        for number in lst:
            if number % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)
        print(f'Even number : {even_numbers} ')
        print(f'Odd number : {odd_numbers}')

    def sentence_duplicate_remover(self, sentence):
        no_duplicate = []

        for word in sentence.split(' '):
            if word not in no_duplicate:
                no_duplicate.append(word)

        new_sentence = ' '.join(no_duplicate)
        redundent = len(sentence.split(' ')) - len(no_duplicate)
        print(new_sentence)
        print(redundent)

    def  range_0_number(self, end):
        for number in range(end + 1):
            print(number)

        
    def print_numbers_divisible(self,num1,num2):
        for x in range(num1 + 1):
            if x % num2 ==0 and x !=0 :
                print(x)

    def print_numbers_divisible_2(self,number1,number2):
        for i in range(101):
            if i % number1 ==0 and i % number2 ==0 and i !=0:
                print(i)


g1 = Game( )



