css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat_message.user{
    b-ckground_color: #2b313e
}
.chat-message.bot{
    background_color: #475063
}
.chat-message .avatar{
    width: 15%;
}
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: 85%;
    padding: 0 1.5rem;
    color: #fff
}
'''
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.freepik.com/free-vector/graident-ai-robot-vectorart_78370-4114.jpg?t=st=1720156637~exp=1720160237~hmac=056be88cd9d32da206d3664e035b4f78127827a96825e7af8cc6fd9c6bd74967&w=1800" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.freepik.com/free-vector/young-woman-long-hair-with-glasses_24877-82904.jpg?t=st=1720157016~exp=1720160616~hmac=c22814eb62cad9f14948e112d50340e047615ea245d35372b318ed032c95e8b9&w=1800">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
