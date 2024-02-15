import React, { useEffect } from "react";
import { useAuthStore } from "../store/auth";
import { logout } from "../utils/auth";
function Logout () {
    useEffect(()=>{
        logout()
    },[])
    return(
        <>
        <div>Logout
            <button onClick={logout}>Logout</button>
        </div>
        </>
    )
}
export default Logout