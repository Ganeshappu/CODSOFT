import streamlit as st
import random
import time

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie! 🤝"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "🎉 You win! 🎉"
    else:
        return "💻 Computer wins! 💻"

def main():
    st.title("🪨📄✂️ Rock, Paper, Scissors Game ✂️📄🪨")
    
    if "user_score" not in st.session_state:
        st.session_state.user_score = 0
    if "computer_score" not in st.session_state:
        st.session_state.computer_score = 0
    
    st.write("### Choose your move:")
    user_choice = st.radio("", ("Rock", "Paper", "Scissors"))
    
    if st.button("🎮 Play!"):
        computer_choice = get_computer_choice()
        st.write("🔄 Generating computer's choice...")
        time.sleep(1)  
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "🎉 You win! 🎉":
            st.session_state.user_score += 1
        elif result == "💻 Computer wins! 💻":
            st.session_state.computer_score += 1
        emoji_map = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🧑 Your Choice")
            st.markdown(f"<div style='border: 2px solid #4CAF50; padding: 20px; border-radius: 10px; text-align: center; font-size: 24px; background-color: #f0f0f0;'>{user_choice} {emoji_map[user_choice]}</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### 💻 Computer's Choice")
            st.markdown(f"<div style='border: 2px solid #F44336; padding: 20px; border-radius: 10px; text-align: center; font-size: 24px; background-color: #f0f0f0;'>{computer_choice} {emoji_map[computer_choice]}</div>", unsafe_allow_html=True)
        
        st.subheader(result)
        
    st.write(f"🏆 **Your Score:** {st.session_state.user_score} | **Computer Score:** {st.session_state.computer_score} 🏆")
    
    if st.button("🔄 Reset Scores"):
        st.session_state.user_score = 0
        st.session_state.computer_score = 0
        st.write("✅ Scores reset!")

if __name__ == "__main__":
    main()