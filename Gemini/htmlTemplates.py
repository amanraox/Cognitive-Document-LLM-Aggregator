css = '''
<style>
.stApp {/* Set your desired background color */
        background-color: linear-gradient(red, yellow);
}

.chat-message {
    padding: 1.5rem; border-radius: 1rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #E3E5E1
}
.chat-message.bot {
    background-color: #17152e
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 90%;
  padding: 0 1.5rem;

    color: #fff;
}
.chat-message.bot .message {
  color: #fff;
}
.chat-message.user .message {
  color: #000;
}
 .header-text {
        background-color: #080134; /* Set your desired background color */
        padding: 15px; /* Adjust padding as needed */
        color: #fff;
        font-size: 40px;
        font-family: "Times New Roman", Times, serif;
        border-radius: 20px; /* Optional: Add border-radius for rounded corners */
    }
st.markdown("---")
    st.text_area("Feedback", value="", height=100)

'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/f80xRML/aed11d6975231b91c8e992c02b8376da-ezgif-com-crop-1.gif" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/3yJw4f8/3sstpm-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
<div>
<p>Made with love by Aman!!</p>
</div>
'''
