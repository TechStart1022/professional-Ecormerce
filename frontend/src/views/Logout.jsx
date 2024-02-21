import React, { useEffect } from 'react';
import { useAuthStore } from '../store/auth';
import { logout } from '../utils/auth';
import { useNavigate } from 'react-router-dom';
function Logout() {
  const navigate = useNavigate();
  useEffect(() => {
    logout();
    navigate('/');
  }, []);
  return (
    <>
      <div>
        Logout
        <button onClick={logout}>Logout</button>
      </div>
    </>
  );
}
export default Logout;
