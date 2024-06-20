import React, { useState } from "react"
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
    const [token, setToken] = useState("")
// handleSubmit function to handle form submission
// Need to send the data to flask backend
    const handleSubmit = (e) => {
        e.preventDefault()
        console.log("Username: ", username)
        console.log("Password: ", password)
        fetch("http://localhost:5000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                setMessage("Login successful")
                setToken(data.token)
                localStorage.setItem("token", data.token)
            } else {
                setMessage(data.message)
            }
        })
    }


    return (
        <>
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
                    <Button className="bg-slate-blueish rounded-md" type="submit">Login</Button>
                </form>
            </CardContent>
            <CardFooter className="flex justify-between">
                <p>Don't have an account?</p>
                <Button className="bg-slate-blueish">Register</Button>
            </CardFooter>
        </Card>
        <p>{message && <p> {message}</p>}</p>
        </>
    )
}
export default Logincard