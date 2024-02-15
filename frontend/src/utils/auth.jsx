import { useAuthStore } from "../store/auth";
import apiInstance from "./axios";
import {jwtDecode} from "jwt-decode"
import Cookies from 'js-cookie'
import axios from "axios";
export const login = async(email, password) => {
    try {
        const {data,status} = await axios.post("http://localhost:8000/api/v1/user/token/",{
            email,
            password
        })
        // console.log(data.access,"refresh_Token")
        if(status == 200){
            // console.log("success get the token")
            setUserAuth(data.access,data.refresh)
        }
        return {data,error:null}
    } catch(error) {
        // console.log(error)
        return {
            data:null,
            // console.log(error)
            // error:error.response.data?.detail || 'Something went wrong'
        }
    }
}
export const register = async(full_name,email, phone,password, password2) => {
    try {
        const {data} = await apiInstance.post('user/register/',{
            full_name,
            email,
            phone,
            password,
            password2
        })
        await login(email,password)
        return {data, error:null}
    } catch(error){
        // console.log(error)
    }
}

export const logout = () => {
    Cookies.remove("accessToken")
    Cookies.remove("refreshToken")
    useAuthStore.getState().setUser(null)
}

export const setUser = async() => {
    const accessToken = Cookies.get('accessToken')
    const refreshToken = Cookies.get('refreshToken')
    if(!accessToken || !refreshToken) {
        return
    }
    if(isAccessTokenExpired(accessToken)){
        const response = await getRefreshToken(refreshToken)
        setAuthUser(response.access,response.refresh)
    } else {
        setUserAuth(accessToken, refreshToken)
    }
}

export const setUserAuth = (accessToken, refresh_token) => {
     Cookies.set('accessToken',accessToken,{
        expires:1,
        secure:true
     })
     Cookies.set('refreshToken',refresh_token,{
        expires:7,
        secure:true
     }) 
     const user = jwtDecode(accessToken) ?? null;
     if(user) {
        useAuthStore.getState().setUser(user)
     }
     useAuthStore.getState().setLoading(false)
}

export const getRefreshToken = async() =>{
    const refresh_token = Cookies.get('refreshToken')
    const response = await apiInstance.post('/user/token/refresh/',{
        refresh:refresh_token
    })
    return response.data
}

export const isAccessTokenExpired = (accessToken) => {
    try{
        const decodedToken = jwtDecode(accessToken)
        return decodedToken.exp <Date.now() /100
    }catch(error){
        return true
    }
}