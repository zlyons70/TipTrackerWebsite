import React, { useState } from "react"
import { useNavigate } from "react-router-dom"
import httpClient from "../../httpClient"
import {
    Card,
    CardContent,
    CardFooter,
    CardHeader,
    CardTitle,
  } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Label } from "@/components/ui/label"
import "../../index.css"

function Logincard() {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [message, setMessage] = useState("")
    const navigate = useNavigate()
// handleSubmit function to handle form submission
// Need to send the data to flask backend
    const handleSubmit = (e) => {
        e.preventDefault()
        console.log("Username: ", username)
        console.log("Password: ", password)
        const loginUser = async () => {
            try {
                const response = await httpClient.post("http://localhost:5000/login", {
                    username: username,
                    password: password
                })
                navigate("/")
            }
            catch (error) {
                if (error === 401)
                    setMessage("Invalid credentials")
                else
                    setMessage("Login failed")
            }
        }
        loginUser()
        }

    const handleRegister = () => {
        navigate("/signup")
    }

    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100 p-4">
        <div className="w-full max-w-md bg-white shadow-lg rounded-lg p-6" style={{ height: '90vh', width: '90vw' }}>
        <Card>
            <CardHeader>
                <CardTitle className="text-center">Login</CardTitle>
            </CardHeader>
            <CardContent>
                <form onSubmit={handleSubmit}>
                    <Label htmlFor="username">
                        Username
                        <Input
                            id="username"
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            placeholder="Username"
                            required
                        />
                    </Label>
                    <Label htmlFor="password">
                        Password
                        <Input
                            id="password"
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="Password"
                            required
                        />
                    </Label>
                    <br />
                    <Button className="bg-slate-blueish rounded-md w-full" type="submit">Login</Button>
                    <div className="flex justify-center">
                    <Button variant="link">Forgot Password?</Button>
                    </div>
                </form>
            </CardContent>
            <CardFooter className="flex flex-col items-center space-y-4 mt-4">
            <Button className="bg-white border border-slate-blueish text-slate-blueish w-full p-2" onClick={handleRegister}>Create New Account</Button>
            </CardFooter>
        </Card>
        {message && <p> {message}</p>}
        </div>
        </div>
    )
}
export default Logincard