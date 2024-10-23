import React, { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom"
import "../../index.css"
import httpClient from "../../httpClient"
import MainNav  from "../../mycomponents/MainNav"
import ShowTipsGraphs from "./showTipsGraphs"

function ViewTips() {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Ensure user is authenticated
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

      </>
    )
}
export default ViewTips;