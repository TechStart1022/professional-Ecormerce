import { useState } from "react"
import axios from "axios"
function ForgotPassword() {
    const [email, setEmail] = useState('')
    const handleSubmit = () => {
        try{
            axios.get(`http://localhost:8000/api/v1/user/password-reset/${email}/`).then((res)=>{
                console.log(res.data)
            })
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