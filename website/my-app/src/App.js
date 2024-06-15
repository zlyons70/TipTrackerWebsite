import React, { useState, useEffect, } from 'react'

function App() {
  const [date, setDate] = useState([{}])

  useEffect(() => {
    fetch("/members").then(res => res.json()).then(data => {
      setDate(data)
      console.log(data)
    }
  )
  }, [])
    
    

  return (
    <div>App</div>
  )
}
export default App
