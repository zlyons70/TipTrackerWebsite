import React, { useState } from "react"
import { useNavigate } from "react-router-dom"
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

function Signupcard() {
    const [email, setEmail] = useState("")
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [confirm_password, setConfirmPassword] = useState("")
    const [message, setMessage] = useState("")
    const [token, setToken] = useState("")
    const navigate = useNavigate()
// handleSubmit function to handle form submission
// Need to send the data to flask backend
    const handleSubmit = (e) => {
        e.preventDefault()
        console.log("Email: ", email)
        console.log("Username: ", username)
        console.log("Password: ", password)
        console.log("Confirm Password: ", confirm_password)
        fetch("http://localhost:5000/sign-up", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email,
                username: username,
                password: password,
                confirm_password: confirm_password
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                setMessage("Registration successful!")
                setToken(data.token)
                localStorage.setItem("token", data.token)
                navigate("/")
                
            } else {
                setMessage(data.message)
            }
        })
    }


    return (
        <div className="flex items-center justify-center min-h-screen bg-gray-100 p-4">
        <div className="w-full max-w-md bg-white shadow-lg rounded-lg p-6" style={{ height: '90vh', width: '90vw' }}>
        <Card>
            <CardHeader>
                <CardTitle className="text-center">Signup</CardTitle>
            </CardHeader>
            <CardContent>
                <form onSubmit={handleSubmit}>
                    <Label htmlFor="email">
                        Email
                        <Input
                            id="email"
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            placeholder="Email"
                            required
                        />
                    </Label>
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
                    <Label htmlFor="password">
                        Confirm Password
                        <Input
                            id="confirm_password"
                            type="password"
                            value={confirm_password}
                            onChange={(e) => setConfirmPassword(e.target.value)}
                            placeholder="Confirm Password"
                            required
                        />
                    </Label>
                    <br />
                    <Button className="bg-slate-blueish rounded-md w-full" type="submit">Register</Button>
                </form>
            </CardContent>
            <CardFooter className="flex justify-center">
            <div className="flex justify-center">
                <Button variant="link">Already Have An Account?</Button>
                </div>
            </CardFooter>
        </Card>
        <p>{message && <p> {message}</p>}</p>
        </div>
        </div>
    )
}
export default Signupcard