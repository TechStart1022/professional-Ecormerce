import React, {useState, useEffect} from 'react'
import { login } from "../utils/auth"
import {useNavigate,Link} from 'react-router-dom'
import { useAuthStore } from "../store/auth"

function Login() {
    const [username, setUsername] = useState('RSG')
    const [password, setPassword] = useState("")
    const [loading, setLoading] = useState(false)
    console.log(username)
    navigate = useNavigate()
    return(
        <div>
            <h2>Welcome to back</h2>
            <p>Login To Continue</p>
        </div>
    )
}

export default Login
