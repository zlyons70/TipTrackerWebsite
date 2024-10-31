import React, { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom"
import "../../index.css"
import httpClient from "../../httpClient"
import MainNav  from "../../mycomponents/MainNav"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import TipCalendar from "./TipCalendar"
import { CalendarIcon } from "@radix-ui/react-icons"
import { Spinner } from "@nextui-org/spinner";

function ViewTips() {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    // Ensure user is authenticated
      (async () => {
          try {
              const response = await httpClient.get('http://localhost:5000/@me');
              setUser(response.data.user);
              console.log(response.data);
              console.log("this got called, user auth in viewtips")
          } catch (error) {
              console.log("not authenticated")
              navigate('/login');
          } finally {
              setLoading(false);
          }
      })();
  }, [navigate]);
  // Doesn't render anything until user is authenticated
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
      <div className="flex justify-center h-full">
      <Tabs defaultValue="Calendar" className="w-[400px]" >
        <TabsList>
          <TabsTrigger value="Calendar" > <CalendarIcon/>Calendar</TabsTrigger>
          <TabsTrigger value="Other">Other</TabsTrigger>
        </TabsList>
        <TabsContent value="Calendar">
          <TipCalendar user={user} />
        </TabsContent>
        <TabsContent value="Other">
          <div>Other content</div>
        </TabsContent>
      </Tabs>
      </div>
      </>
    )
}
export default ViewTips;