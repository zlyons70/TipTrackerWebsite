import React from 'react'
import ReactDOM from 'react-dom/client'
import Dashboard  from './Dashboard'
import {NextUIProvider} from '@nextui-org/react'
ReactDOM.createRoot(document.getElementById('root')).render(
    // This is the JSX code that will be rendered in the /home/ root URL
    // During development I need to use /home/ to access the home page
    <React.StrictMode>
        <NextUIProvider>
            <Dashboard />
        </NextUIProvider>
    </React.StrictMode>,
  )
