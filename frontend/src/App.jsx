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
import CreatePassword from './views/CreatePassword'
import StoreHeader from './base/StoreHeader'
import StoreFooter from './base/StoreFooter'
import Products from './views/Products'
import ProductDetail from './views/ProductDetail'
function App() {
  return (
    <>
    <BrowserRouter>
    <StoreHeader />
      <Routes>
        <Route path='/login' element = {<Login />} />
        <Route path='/register' element = {<Register />} />
        <Route path='/' element = {<Dashboard />} />
        <Route path='/logout' element = {<Logout />} />
        <Route path='/forgotpassword' element = {<ForgotPassword />} />
        <Route path='/create-new-password' element = {<CreatePassword />} />
        <Route path='/product' element = {<Products />} />
        <Route path='/detail/:slug' element = {<ProductDetail />} />
      </Routes>
      <StoreFooter />
    </BrowserRouter>
        
    </>
  )
}

export default App
