import React, { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom"
import "../../index.css"
import httpClient from "../../httpClient"
import MainNav  from "../../mycomponents/MainNav"
import AddTips  from "@/mycomponents/AddTips"
function Dashboard() {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);

  useEffect(() => {
      (async () => {
          try {
              const response = await httpClient.get('//localhost:5000/@me');
              setUser(response.data.user);
              console.log(response.data);
          } catch (error) {
              console.log("not authenticated")
              navigate('/login');
          }
      })();
  }, [navigate]);
    return (
      <>
      <MainNav />
      <AddTips user={user}/>
      </>
    )
}
export default Dashboard;