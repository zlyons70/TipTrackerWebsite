import React, { useState } from "react"
import { useNavigate } from "react-router-dom"
import httpClient from "../httpClient"
import {
  Navbar, 
  NavbarBrand, 
  NavbarContent, 
  NavbarItem, 
  NavbarMenuToggle,
  NavbarMenu,
  NavbarMenuItem
} from "@nextui-org/navbar";
import { Link, Button } from "@nextui-org/react";
import "../index.css"
import { useLocation } from "react-router-dom";
function MainNav() {
    const location = useLocation();
    const navigate = useNavigate();
    const logoutUser = async () => {
      await httpClient.post("http://localhost:5000/logout")
      navigate("/login")
       
    }
    return (
      <> 
      <Navbar isBordered isBlurred={false}>
        <NavbarBrand>HI</NavbarBrand>
        <NavbarContent className="sm:flex gap-4" justify="center">
          <NavbarItem isActive={location.pathname === '/'}>
            <Link color="foreground" href="/">
              Home
            </Link>
          </NavbarItem>
          <NavbarItem isActive={location.pathname === '/viewtips'}>
            <Link href="viewtips" aria-current="page">
              View Tips
            </Link>
          </NavbarItem>
          <NavbarItem isActive={location.pathname === '/edit'}>
            <Link href="edit" aria-current="page">
              Edit Tips
            </Link>
          </NavbarItem>
          <NavbarItem isActive={location.pathname === '/account'}>
            <Link color="foreground" href="/account">
              Account
            </Link>
          </NavbarItem>
        </NavbarContent>
        <NavbarContent justify="end">
          <NavbarItem>
            <Button onPress={logoutUser} color="primary" href="#" variant="flat">
              Sign Out
            </Button>
          </NavbarItem>
        </NavbarContent>
    </Navbar>
      </>
    )
}
export default MainNav;