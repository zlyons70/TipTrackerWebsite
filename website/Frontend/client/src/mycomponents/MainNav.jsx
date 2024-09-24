import React, { useState } from "react"
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

    return (
      <> 
      <Navbar isBordered isBlurred={false}>
        <NavbarBrand>HI</NavbarBrand>
        <NavbarContent className="sm:flex gap-4" justify="center">
          <NavbarItem isActive={location.pathname === '/'}>
            <Link color="foreground" href="#">
              Home
            </Link>
          </NavbarItem>
          <NavbarItem isActive={location.pathname === '/edittips'}>
            <Link href="#" aria-current="page">
              Edit Tips
            </Link>
          </NavbarItem>
          <NavbarItem isActive={location.pathname === '/account'}>
            <Link color="foreground" href="#">
              Account
            </Link>
          </NavbarItem>
        </NavbarContent>
        <NavbarContent justify="end">
          <NavbarItem>
            <Button as={Link} color="primary" href="#" variant="flat">
              Sign Out
            </Button>
          </NavbarItem>
        </NavbarContent>
    </Navbar>
      </>
    )
}
export default MainNav;