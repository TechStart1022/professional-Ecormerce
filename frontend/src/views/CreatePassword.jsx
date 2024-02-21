import { useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function CreatePassword() {
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [searchParam] = useSearchParams();

  const otp = searchParam.get('otp');
  const uidb64 = searchParam.get('uidb64');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (password !== confirmPassword) {
      alert('Password not match');
    } else {
      // console.log(password,otp,uidb64)
      const formdata = { password, otp, uidb64 };
      console.log(formdata, 'formdata ');
      try {
        await axios
          .post('http://localhost:8000/api/v1/user/password-change/', formdata)
          .then((res) => {
            console.log(res.data);
            alert('password changed successfully');
            navigate('/login');
          });
      } catch (err) {
        console.log(err);
      }
    }
  };

  return (
    <>
      <h1>Create Password</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="password"
          name="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="password"
          required
        />
        <br />
        <br />
        <input
          type="password"
          name="confirmPassword"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          placeholder="confirm password"
          required
        />
        <br />
        <br />
        <button type="submit">Create new password</button>
      </form>
    </>
  );
}

export default CreatePassword;
