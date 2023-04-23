import streamlit as st
import random

# Define the quiz question and answer
quiz_data = {
    "What is the currency of japan?": {
        'options': ["Yen", "Dollar", "Pound", "Euro"],
        'answer' : 'Yen'
    },
    "What is the capital of Australia?": {
        'options':["Canberra", "Sydney", "Melbourne", "Rome"],
        'answer' :'Canberra'
    },
    "Where is the centre for cellular and molecular biology situated?": {
        'options':["Hyderabad", "Patna", "Jaipur", "New Delhi"],
        'answer':'Hyderabad'
    },
    "Where is the railway staff college located?": {
        'options': ["Vadodara", "Pune", "Allahabad", "New Delhi"],
        'answer': 'Vadodara'
    },
    "January 15 is celebrated as at?": {
        'options': ["Republic Day","Army Day", "Teacher's Day", "Earth Day"],
        'answer': 'Army Day'
    }
}

# Function to display quiz question and get the answers

num_correct = 0
num_incorrect = 0
user_answer_list = {}
def display_quiz_questions(quiz_data):
    num_questions = len(quiz_data)

    for question, data in quiz_data.items():
        st.write(question)
        user_answer = st.selectbox("Select your answer:", data['options'])
        user_answer_list[question] = user_answer
    return num_correct, num_incorrect

# Streamlit app

def main():
    st.title("Quiz Game")
    st.write("Select your answers:")

    num_correct, num_incorrect = display_quiz_questions(quiz_data)

    if st.button("check answers"):
        for question, data in quiz_data.items():
            if data['answer'] == user_answer_list[question]:
                num_correct +=1
            else:
                num_incorrect +=1

        st.write(num_correct)    
        st.write(num_incorrect)    
if __name__ == "__main__":
    main()