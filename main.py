import random
file = open("words.txt")
#https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt
word_list = file.readlines()
file.close()
word_list = [word.replace('\n', '') for word in word_list]

def one_game():
    word_target = random.choice(word_list)
    cnt = 0
    while True:
        cnt += 1
        print(str(cnt) + "/6")
        if cnt > 6:
            print("※※※※※※GAME OVER※※※※※※")
            return 0

        word_input = str(input("Your guess:")).lower()

        if word_input == "exit":
            print("※※※※※※※EXITING THE GAME※※※※※※ ")
            return 0

        if len(word_input) != 5:
            print("The length of the word is not 5! Try again.")
            cnt -= 1
            continue

        if word_input == word_target:
            print("※※※※※※※Congrats!※※※※※※")
            return 7 - cnt
        elif word_input not in word_list:
            print("The word is not listed. Please Try again.")
            cnt -= 1
            continue

        word_output = ""
        for i in range(5):
            if word_input[i] == word_target[i]:
                word_output += "○"
            elif word_input[i] in word_target:
                word_output += "△"
            else:
                word_output += "X"
            print(word_output)

def run():
    score = 0
    print("Type 'Exit' if you want to finish the game")
    while True:
        game = one_game()
        score += game
        print("YOUR SCORE: " + str(game) + " TOTAL SCORE: " + str(score))
        if game == -1:
            break
    print("SCORE: " + str(score))

run()
