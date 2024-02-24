// HomePage.tsx
import React from 'react';
import './HomePage.css';

const HomePage: React.FC = () => {
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
    }, 100); // Adjust the interval to control typing speed

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
        <button className="login-button">Login</button>
        <button className="signup-button">Signup</button>
      </div>
    </div>
  );
}

export default HomePage;
