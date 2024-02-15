import {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom'
import { register } from '../utils/auth'
import MainWrapper from '../layout/MainWrapper'
function Register() {
    const [fullname, setFullname] = useState()
    const [email, setEmail] = useState('')
    const [mobile, setMobile] = useState('')
    const [username,setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [password2,setPassword2] = useState('')

    const [isLoading,setIsLoading] = useState(false)
    const navigate = useNavigate()

    const resetForm = () => {
        setFullname('')
        setMobile('')
        setUsername('')
        setPassword('')
        setPassword2('')
    }
    const hanlder = async(e) => {
        e.preventDefault()
        setIsLoading(true)
        const {error} =await register(fullname, email, mobile, username, password, password2)
        if(error){
            alert(JSON.stringify(error))
            resetForm()
        } else {
            navigate('/login')
        }
        setIsLoading(false)
    }

    useEffect(()=>{

    },[])

    return (
        <>
        <form onSubmit={hanlder}>
            <input
                type='text'
                name='fullname'
                placeholder='fullname'
                value={fullname}
                onChange={(e)=>setFullname(e.target.value)}
            />
            <br/>
            <br/>
            <input
                type='email'
                name='email'
                placeholder='email'
                value={email}
                onChange={(e)=>setEmail(e.target.value)}
            />
            <br/>
            <br/>            
            <input
                type='text'
                name='mobile'
                placeholder='mobile'
                value={mobile}
                onChange={(e)=>setMobile(e.target.value)}
            />
            <br/>
            <br/>
            <input
                type='password'
                name='password'
                placeholder='password'
                value={password}
                onChange={(e)=>setPassword(e.target.value)}
            />
            <br/>
            <br/>
            <input
                type='password'
                name='password2'
                placeholder='password2'
                value={password2}
                onChange={(e)=>setPassword(e.target.value)}
            />
            <br/>
            <br/>
            <button type='submit'>Register</button>
        </form> 
        </>
    )
}
export default Register