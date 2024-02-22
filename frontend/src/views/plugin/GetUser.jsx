import Cookie from 'js-cookie';
import {jwtDecode} from 'jwt-decode';

function UserData() {
  let access_token = Cookie.get('accessToken');
  let refresh_token = Cookie.get('refreshToken');
  console.log(access_token,"accesstoken")

  if (access_token && refresh_token) {
    const token = refresh_token;
    const decoded = jwtDecode(token);
    return decoded;
  } else {
    console.log('User Token Does not match');
    return;
  }
}

export default UserData;
