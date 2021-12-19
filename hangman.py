from random import randrange
from string import ascii_lowercase


msg_ = [""] * 20
msg_[0] = "H A N G M A N"
msg_[1] = 'The game will be available soon.'
msg_[2] = 'Guess the word {}:'
msg_[3] = 'You survived!'
msg_[4] = 'You lost!'
msg_[5] = 'Input a letter:'
msg_[6] = "That letter doesn't appear in the word"
msg_[7] = '\nThanks for playing!'
msg_[8] = "We'll see how well you did in the next stage"
msg_[9] = "No improvements"
msg_[10] = "You guessed the word {}!"
msg_[11] = "You should input a single letter"
msg_[12] = "You've already guessed this letter"
msg_[13] = "Please enter a lowercase English letter"
msg_[14] = 'Type "play" to play the game, "exit" to quit:'
# msg_[1] = ""

sekret_list = ['python', 'java', 'kotlin', 'javascript']
sekret = sekret_list[randrange(len(sekret_list))]
letters = set()
print(msg_[0])

while 1:
    mode = input(msg_[14]).lower()
    if mode == "exit":
        break
    if mode != "play":
        continue
    

    step = 8
    while step > 0 and not set(sekret).issubset(letters):
        vis = ""
        for s in sekret:
            vis += s if s in letters else "-"
        print()
        print(vis)
        # print(step)
        i = input(msg_[5])
        if len(i) != 1:
            print(msg_[11])
            continue
        elif i not in ascii_lowercase:
            print(msg_[13])
            continue

        elif i in letters:
            print(msg_[12])
            continue

        letters.add(i)
        if i not in sekret:
            step -= 1
            print(msg_[6])
            
    if set(sekret).issubset(letters):
        print(msg_[10].format(sekret))
        print(msg_[3])
    else:
        print(msg_[4])
    print()

# -----------
