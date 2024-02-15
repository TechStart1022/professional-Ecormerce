import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Login from './views/login'
import Register from './views/register'
import {BrowserRouter, Route, Routes} from "react-router-dom"
import Dashboard from './views/Dashboard'
import Logout from './views/Logout'
import ForgotPassword from './views/ForgetPassword'
function App() {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path='/login' element = {<Login />} />
        <Route path='/register' element = {<Register />} />
        <Route path='/' element = {<Dashboard />} />
        <Route path='/logout' element = {<Logout />} />
        <Route path='/forgotpassword' element = {<ForgotPassword />} />
      </Routes>
    </BrowserRouter>
        
    </>
  )
}

export default App
