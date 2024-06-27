import React, { useState } from "react"
import "../../index.css"
import MainNav  from "../../mycomponents/MainNav"
import AddTips  from "@/mycomponents/AddTips"
function Dashboard() {
    return (
      <>
      <MainNav />
      <AddTips />
      </>
    )
}
export default Dashboard;