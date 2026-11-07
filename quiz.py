import pandas as pd
import os

def clear():
    os.system('cls' if os.name =='nt' else 'clear')

def run_quiz(df):
    clear()
    #df = pd.read_csv(filename)
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
    questions=pd.read_csv('cards.csv')
    while True:
        clear()
        print("welcome to mlquiz!\n")
        print("1. take full quiz")
        print("2. choose a category")
        
        if os.path.exists('mistakes.csv'):
            print("3. study mistakes")
            
        print("4. quit")

        choice = input("\nselect an option: ")

        if choice == '1':
            run_quiz(questions)
            input("\npress enter to return to menu")
        elif choice =='2':
            categories=questions['category'].unique()
            print("\ncategories:")
            for i in range(len(categories)):
                print(f"{i+1}. {categories[i]}")
            choice=input("\npick a number ")

            try:
                index=int(choice)-1
                if 0 <= index < len(categories):
                    selected=categories[index]
                    filtered = questions[questions['category']==selected]
                    run_quiz(filtered)
                    input("\npress enter to return to menu")
                else:
                    print("invalid number")
                    input("press enter to reenter number")
            except ValueError:
                print("please type a number")
                input("press enter to try again")
        
        elif choice == '3' and os.path.exists('mistakes.csv'):
            mistakes_df=pd.read_csv('mistakes.csv')
            run_quiz(mistakes_df)
            input("\npress enter to return to menu")
        elif choice=='4':
            break

if __name__ == "__main__":
    main()