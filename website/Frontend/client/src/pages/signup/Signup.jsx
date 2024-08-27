import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from "react-router-dom";
import Signupcard from './Signupcomp.jsx'
ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <BrowserRouter>
        <Signupcard />
        </BrowserRouter>
    </React.StrictMode>,
  )
