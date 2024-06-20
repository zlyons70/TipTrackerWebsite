import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

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
  <Card>
    <CardHeader>
      <CardTitle>Card Title</CardTitle>
      <CardDescription>Card Description</CardDescription>
    </CardHeader>
    <CardContent>
      <p>Card Content</p>
    </CardContent>
    <CardFooter>
      <p>Card Footer</p>
    </CardFooter>
  </Card>

    </>
)
}

export default App
