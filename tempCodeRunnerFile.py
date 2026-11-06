import pandas as pd
import os

def clear():
    os.system('cls' if os.name =='nt' else 'clear')

def run_quiz(filename):
    clear()
    df = pd.read_csv(filename)
    score = 0
    wrong = []

    for index, row in df.iterrows():
        print(f"question {index+1} {row['question']}")
        if row['type'] == 'mcq':
            print(f"a) {row['optiona']}")
            print(f"b) {row['optionb']}")
            print(f"c) {row['optionc']}")
            print(f"d) {row['optiond']}")
            
        answer = input("\nyour answer ")
        answer = answer.strip().lower()

        if row['type'] == 'mcq':
            if answer == 'a':
                answer = str(row['optiona']).strip().lower()
            elif answer == 'b':
                answer = str(row['optionb']).strip().lower()
            elif answer == 'c':
                answer = str(row['optionc']).strip().lower()
            elif answer == 'd':
                answer = str(row['optiond']).strip().lower()
                
        if answer == str(row['correctanswer']).strip().lower():
            print("correct")
            score += 1
        else:
            print(f"wrong answer, correct answer is {row['correctanswer']}")
            wrong.append(row)

        input("\npress enter for next question")
        clear()

    print(f"quiz is over: {score}/{len(df)}")

    if len(wrong) > 0:
        wrong_df = pd.DataFrame(wrong)
        wrong_df.to_csv('mistakes.csv', index=False)
        print(f"you got {len(wrong)} questions wrong, saved as mistakes.csv")
    else:
        if os.path.exists('mistakes.csv'):
            os.remove('mistakes.csv')
        print("perfect score! no mistakes")

def main():
    while True:
        clear()
        print("welcome to mlquiz!\n")
        print("1. take full quiz")
        
        if os.path.exists('mistakes.csv'):
            print("2. study mistakes")
            
        print("3. quit")

        choice = input("\nselect an option: ")

        if choice == '1':
            run_quiz('cards.csv')
            input("\npress enter to return to menu")
        elif choice == '2' and os.path.exists('mistakes.csv'):
            run_quiz('mistakes.csv')
            input("\npress enter to return to menu")
        elif choice == '3':
            break
        else:
            print("invalid choice")
            input("press enter to try again")

if __name__ == "__main__":
    main()