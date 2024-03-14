css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
}
.chat-message.user {
    background-color: #F0F2F6
}
.chat-message.bot {
    background-color: #DCDEE2
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 40px;
  max-height: 40px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 100%;
  padding: 0 1.5rem;
  color: #000;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <b>AI:</b>
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <b>USUÁRIO:</b>
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
