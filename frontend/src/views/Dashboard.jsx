import React,{useState,useEffect} from 'react'
import { useAuthStore } from '../store/auth'
import { useNavigate,Link } from 'react-router-dom'


function Dashboard(){

    const [isLoggedIn, setIsLoggedIn] = useState(useAuthStore((state) => state.setLoggedIn))
    
    return (
        <>
        {!isLoggedIn 
            ?<div>
                <Link to={'/login'}>login</Link><br/>
                <Link to={'/register'}>Register</Link>
            </div> 
            :<div>
                <h1>Home page</h1>
                <Link to={'/logout'}>Logout</Link>
            </div>
        }
        </>
    )
}
export default Dashboard