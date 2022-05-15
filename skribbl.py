#This program displays the possible keywords that you're supposed to guess in skribbl.io 
#First put the custom keywords in the array
#Then program asks to enter the number of characters in word that you're trying to guess
#REMEMBER SPACE COUNTS if the word is "____ ___" Then number of characters should be 8
#Then program displays every possible keyword that fits the requirement from array.

# list keywords of scribble here in array
keywords = ["lion", "fish", "Ferret", "goat", "crab", "wolverine", "cow", "horse", "crow", "meerkat", "seal", "llama", "leopard", "rhinoceros", "warthog", "ape", "chipmunk", "elephant", "deer", "walrus", "panda", "pig", "parakeet", "beaver", "puma", "bison", "Eagle", "owl", "fox", "anteater", "groundhog", "lamb", "parrot", "panther", "coyote", "koala", "ram", "Squirrel", "moose", "Kitten", "Otter", "octopus", "iguana", "sheep", "dog", "giraffe", "camel", "kangaroo", "toad", "Tiger", "sloth", "raccoon", "alligator", "weasel", "rooster", "jaguar", "polar bear", "snake", "wombat", "bear", "wolf", "chameleon", "hedgehog", "newt", "donkey", "salamander", "mole", "bat", "Gorilla", "skunk", "rabbit", "pony", "chimpanzee", "whale", "opossum", "monkey", "platypus", "buffalo", "zebra", "dolphin", "cat", "bull", "rat", "chinchilla", "reindeer", "armadillo", "Antelope", "turtle", "puppy", "hippopotamus", "porcupine", "starfish", "hamster", "crocodile", "chicken", "lemur", "bumble bee", "ox", "bald eagle", "cheetah", "frog", "orangutan", "lizard", "yak", "mouse", "duck", "seahorse", "penguin", "ant", "spider", "ladybug", "butterfly", "worm", "dragonfly", "flamingo", "jellyfish", "moth", "ostrich", "peacock", "shark"]

def skribbl():
    # asking for num of characters in the word, remember space counts as well
    value = input("Enter length of word.")

    # converting user input to integer
    try:
        length = int(value)
    except:
        print ("Enter integer value only")
        skribbl()

    # iterating through every array element
    for index in range(len(keywords)):
        
        # checking the user input length with array element length      
        if (len(keywords[index]) == length):
        
        # printing keywords whose length matches with the user input length
            print (keywords[index])

skribbl()
