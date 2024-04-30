
# This class just for the game data
class Data: 
    counter = 12   # counter for the guest player
    correctGuess = "" # save the correct characters
   
    def __init__(self):
        # get elements of the player
        self.hostplayer = input('Please enter your name : ')
        self.word = input(f"Hi, {self.hostplayer}, please Enter a word : ")
        self.guestplayer = input('Hi , Please enter your name : ')
        self.char = None
        
        
        
# Just for data controller ..
class Controller(Data):
    
    def check_answer(self):# This fun is for character checking
        if self.char in self.word:
            return True, f"{self.guestplayer}: your guess is correct !!"
        return False, f"{self.guestplayer}: your guess is not correct !! please guess again ..."
    
    # This function is for the correct guess checking, 
    # if the guess was correct then add the character to the correct guess variable
    def correct_guess(self):  
        reply = self.check_answer()
        if reply[0]:
            if self.char not in Data.correctGuess:
                Data.correctGuess+=self.char
            else:
                print(f"There is {self.char} character in correct guess")
                
    def not_correct_guess(self): # This fun for wrong guess checking,
        reply = self.check_answer()
        if reply[0]== False:
            Data.counter-=1
            print(f"number of remaining guess :{Data.counter}")
            
 # This is for the game logic
class GameLogic(Controller, Data):
        
    def start(self):
        while True:
            # if the player can guess all the characters of the word, the player wins ! and game end
            if len(Data.correctGuess)==len(self.word):
                print(f"{self.guestplayer} you win the game, {self.word}")
                break
            # if counter ==0 then game end 
            # and the player loses
            if Data.counter==0:
                print(f"o.h..o.h!! {self.guestplayer} you lost the game,I'm sarry..!! , correct word is {self.word}")
                break
            # input of the guest player for character
            self.char = input(f"{self.guestplayer}, Please enter a guess : word length {len(self.word)} :: ")
            
            player_reply = self.check_answer()
            if player_reply[0]:
                print(player_reply[1])
                self.correct_guess()
            else:
                print(player_reply[1])
                self.not_correct_guess()
                
# create instance of class GameLogic

obj_1 = GameLogic()
obj_1.start()       
    
        
            
        
        
            
                
            
            
        
        
    