import pandas as pd
import os

def clear():
    os.system('cls' if os.name =='nt' else 'clear')
def main():
    clear()
    print("welcome test")
    df = pd.read_csv('cards.csv')
    score=0

    for index, row in df.iterrows():
        print(f"question {index+1} {row['question']}")
        if row['type'] =='mcq':
            print(f"a) {row['optiona']}")
            print(f"b) {row['optionb']}")
            print(f"c) {row['optionc']}")
            print(f"d) {row['optiond']}")
        answer = input("ypur answer")

        if answer.strip().lower()== str(row['correctanswer']).strip().lower():
            print("correct")
            score +=1
        else:
            print(f"wrong, correct: {row['correctanswer']}\n")
        input("press enter")
        clear()
    print(f"over, score: {score}/{len(df)}")
if __name__=="__main__":
    main()
                                        
