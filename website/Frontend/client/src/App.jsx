import {BrowserRouter, Routes, Route} from 'react-router-dom'
import './App.css'
import Dashboard from './pages/home/Dashboard'
import Logincard from './pages/Login/Logincomp'
import Signupcard from './pages/signup/Signupcomp'
import ViewTips from './pages/viewtip/ViewTips'

function App() {
  // const [count, setCount] = useState(0)
  // // API calls are asynchronous, so we need to use useEffect to call the function
  // const fetchAPI = async () => {
  //   const response = await axios.get('http://127.0.0.1:5000/api/members')
  //   // logs the response data to the console
  //   console.log(response.data.members)
  // }
  // // useEffect means it only runs on the initial component render
  // // passing the empty array as the second argument means it only runs once
  // useEffect(() => {
  //   fetchAPI()
  // }, [])

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/login" element={<Logincard />} />
        <Route path="/signup" element={<Signupcard />} />
        <Route path="/viewtips" element={<ViewTips />} />
        <Route path="*" element={<h1>404 Not Found</h1>} />
      </Routes>
    </BrowserRouter>
)
}

export default App
