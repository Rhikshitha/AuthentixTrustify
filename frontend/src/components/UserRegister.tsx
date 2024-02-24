// AuthPage.tsx
import React from 'react';

const UserRegsiter: React.FC = () => {
  return (
    <div className="auth-container">
      <div className="left-panel">
        <h2>Login</h2>
        <form>
          <label htmlFor="email">Email:</label>
          <input type="email" id="email" className="input-field" />
          <label htmlFor="password">Password:</label>
          <input type="password" id="password" className="input-field" />
          <button type="submit" className="submit-button">Login</button>
        </form>
      </div>
      <div className="right-panel">
        <h2>Sign Up</h2>
        <form>
          <label htmlFor="signup-email">Email:</label>
          <input type="email" id="signup-email" className="input-field" />
          <label htmlFor="signup-password">Password:</label>
          <input type="password" id="signup-password" className="input-field" />
          <button type="submit" className="submit-button">Sign Up</button>
        </form>
      </div>
    </div>
  );
}

export default UserRegsiter;
