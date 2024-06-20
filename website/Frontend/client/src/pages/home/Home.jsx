import React from 'react'
import ReactDOM from 'react-dom/client'

ReactDOM.createRoot(document.getElementById('root')).render(
    // This is the JSX code that will be rendered in the /home/ root URL
    // During development I need to use /home/ to access the home page
    <React.StrictMode>
        <h1>Home</h1>
    </React.StrictMode>,
  )
