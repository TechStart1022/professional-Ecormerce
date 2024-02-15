import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Login from './views/login'
import Register from './views/register'
import {BrowserRouter, Route, Routes} from "react-router-dom"
function App() {
  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path='/login' element = {<Login />} />
        <Route path='/register' element = {<Register />} />
      </Routes>
    </BrowserRouter>
        
    </>
  )
}

export default App
