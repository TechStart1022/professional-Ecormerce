import { useState } from "react"
import { useNavigate } from "react-router-dom"
import axios from "axios"
function ForgotPassword() {
    const navigate = useNavigate()
    const [email, setEmail] = useState('')
    const handleSubmit = async() => {
        try{
            await axios.get(`http://localhost:8000/api/v1/user/password-reset/${email}/`).then((res)=>{
                console.log(res.data)
            })
            alert('You sent email for reset password')
        }catch(error){
            console.log(error)
        }
    }
    return (
        <div>
            <h1>Forgot Password</h1>
            <input 
                onChange={(e)=>setEmail(e.target.value)}
                type="email" 
                placeholder="Enter email"
                name="email"
                required
            />
            <br/>
            <br/>
            <button onClick={handleSubmit}>Reset Password</button>
        </div>
    )
}
export default ForgotPassword