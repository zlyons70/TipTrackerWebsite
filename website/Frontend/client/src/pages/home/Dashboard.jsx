import React, { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom"
import "../../index.css"
import httpClient from "../../httpClient"
import MainNav  from "../../mycomponents/MainNav"
import AddTips  from "@/mycomponents/AddTips"
import { Spinner } from "@nextui-org/spinner";
function Dashboard() {
    const navigate = useNavigate();
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    useEffect(() => {
      (async () => {
          try {
              const response = await httpClient.get('//localhost:5000/@me');
              setUser(response.data.user);
              console.log(response.data);
          } catch (error) {
              console.log("not authenticated")
              navigate('/login');
          } finally {
              setLoading(false);
          }
      })();
  }, [navigate]);
    if (loading) {
        return (
            <>
            <MainNav />
            <div className="flex justify-center h-full">
            <Spinner size="large" />
            </div>
            </>
        )
    }
    return (
      <>
      <MainNav />
      <AddTips user={user}/>
      </>
    )
}
export default Dashboard;