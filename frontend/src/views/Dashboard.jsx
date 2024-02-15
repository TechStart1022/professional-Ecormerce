import React,{useState,useEffect} from 'react'
import { useAuthStore } from '../store/auth'
import { useNavigate } from 'react-router-dom'


function Dashboard(){

    const [isLoggedIn, setIsLoggedIn] = useState(useAuthStore(state=>state.setLoggedIn))
    console.log(isLoggedIn())
    return (
        <>
        <div>
            <h1>welcome to dashboard</h1>
        </div>
        </>
    )
}
export default Dashboard