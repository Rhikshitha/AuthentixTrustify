// Login.tsx
import React from 'react';

const UserLogin: React.FC = () => {
  return (
    <div className="login-container">
      <h2>Login</h2>
      <form>
        <label>
          Email:
          <input type="email" className="input-field" />
        </label>
        <label>
          Password:
          <input type="password" className="input-field" />
        </label>
        <button type="submit" className="submit-button">Login</button>
      </form>
    </div>
  );
}

export default UserLogin;
