import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/assets/vite.svg'
import './App.css'
import axios from 'axios'

function App() {
  const [count, setCount] = useState(0)
  // API calls are asynchronous, so we need to use useEffect to call the function
  const fetchAPI = async () => {
    const response = await axios.get('http://127.0.0.1:5000/api/members')
    // logs the response data to the console
    console.log(response.data.members)
  }
  // useEffect means it only runs on the initial component render
  // passing the empty array as the second argument means it only runs once
  useEffect(() => {
    fetchAPI()
  }, [])

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
