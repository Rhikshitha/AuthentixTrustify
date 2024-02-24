import React from 'react';
import './HomePage.css';
import ChatBot from './ChatBot';

const Chat: React.FC = () => {
  const sentence = 'AuthentixTrustify: Pioneering Deep Learning for Document Processing and Verification';
  const [typedSentence, setTypedSentence] = React.useState('');
  const [currentIndex, setCurrentIndex] = React.useState(0);

  React.useEffect(() => {
    const interval = setInterval(() => {
      if (currentIndex < sentence.length) {
        setTypedSentence((prev) => prev + sentence[currentIndex]);
        setCurrentIndex((prev) => prev + 1);
      } else {
        setTypedSentence('');
        setCurrentIndex(0);
      }
    }, 100); 

    return () => clearInterval(interval);
  }, [currentIndex, sentence.length]);

  return (
    <div className="home-container">
      <div className="left-panel">
        <div className="top-left">
          <h1>AuthentixTrustify</h1>
        </div>
        <h2>{typedSentence}</h2>
      </div>
      <div className="right-panel">
        <ChatBot/>
      </div>
    </div>
  );
}

export default Chat;
