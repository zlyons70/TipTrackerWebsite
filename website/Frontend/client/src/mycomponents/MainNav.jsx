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

function MainNav() {
    return (
      <>
      <Navbar isBordered isBlurred={false}>
        <NavbarBrand>HI</NavbarBrand>
        <NavbarContent className="sm:flex gap-4" justify="center">
          <NavbarItem isActive>
            <Link color="foreground" href="#">
              Home
            </Link>
          </NavbarItem>
          <NavbarItem>
            <Link href="#" aria-current="page">
              Edit Tips
            </Link>
          </NavbarItem>
          <NavbarItem>
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