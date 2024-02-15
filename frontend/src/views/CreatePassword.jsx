import { useState } from "react";
import { useSearchParams } from "react-router-dom";

function CreatePassword() {
    const [password,setPassword] = useState('')
    const [confirmPassword, setConfirmPassword] = useState('')
    const [searchParam] = useSearchParams()
    const otp = searchParam.get('otp')
    const uidb64 = searchParam.get('uidb64')
    const handleSubmit = (e) => {
        console.log(otp)
        console.log(uidb64)
        e.preventDefault()
        if(password !== confirmPassword){
            alert('Password not match')
        }else{
            alert('password processing...')

        }
    }

    return(
        <>
        <h1>Create Password</h1>
        <form onSubmit={handleSubmit}>
            <input 
                type="password"
                name="password"
                value={password}
                onChange={(e)=>setPassword(e.target.value)}
                placeholder="password"
                required
            />
            <br/>
            <br/>
            <input
                type="password"
                name="confirmPassword"
                value={confirmPassword}
                onChange={(e)=>setConfirmPassword(e.target.value)}
                placeholder="confirm password"
                required
            />
            <br/>
            <br/>
            <button type="submit">Create new password</button>
        </form>
        </>
    )
}

export default CreatePassword