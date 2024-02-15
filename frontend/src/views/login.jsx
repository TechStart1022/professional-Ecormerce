import React, {useState, useEffect} from 'react'
import { login } from "../utils/auth"
import {useNavigate,Link} from 'react-router-dom'
import { useAuthStore } from "../store/auth"

function Login() {
    const [email, setEmail] = useState('RSG')
    const [password, setPassword] = useState("")
    const [loading, setLoading] = useState(false)
    const isLoggedIn = useAuthStore((state) => state.setLoggedIn)
    const logginUser = useAuthStore((state)=>state.allUserData)
    
    const navigate = useNavigate()
    useEffect(()=>{
        console.log(isLoggedIn())
        console.log(logginUser)
        if(isLoggedIn()){
            navigate('/')
        }
    },[isLoggedIn()])
    const resetForm = () => {
        setEmail('')
        setPassword('')
    }
    const handleLogin = (e) => {
        e.preventDefault()
        setLoading(true)
        const {error} = login(email,password)
        if(error){
            resetForm()
        }
        setLoading(false)
    }
    // const navigate = useNavigate()
    return(
        <div>
            <h2>Welcome to back</h2>
            <p>Login To Continue</p>
            <form onSubmit={handleLogin}>
                <input 
                    type='text' 
                    id='email' 
                    name='email' 
                    value={email}
                    onChange={(e) => setEmail(e.target.value)} 
                />
                <br/>
                <br/>
                <input 
                    type='password'
                    id='password'
                    name='password'
                    value={password}
                    onChange={(e)=>setPassword(e.target.value)}
                />
                <br/>
                <br/>
                <button type='submit'>Login</button>
            </form>
            <hr/>
            <br/>
            <Link to={'/forgotpassword'}>Forget Password</Link>
        </div>
    )
}

export default Login
