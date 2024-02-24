import React, { useState } from 'react';
import './ChatBot.css';

interface Message {
  text: string;
  isUser: boolean;
}

const ChatBot: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');

  const sendMessage = async () => {
    if (!inputValue.trim()) return;
    const newMessages = [...messages, { text: inputValue, isUser: true }];
    setMessages(newMessages);
    console.log(inputValue)
    try {
      const response = await fetch('http://127.0.0.1:8000/send_message/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: inputValue }),
      });
      const data = await response.json();
      setMessages([...newMessages, { text: data.message, isUser: false }]);
    } catch (error) {
      console.error('Error sending message:', error);
    }
    setInputValue('')
  };
  

  return (
    <div className="App">
      <div className="messages">
        {messages.map((message, index) => (
          <div key={index} className={`message ${message.isUser ? 'user' : 'bot'}`}>
            {message.text}
          </div>
        ))}
      </div>
      <div className="input">
        <input
          type="text"
          placeholder="Type a message..."
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default ChatBot;
