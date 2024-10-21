import React from "react";
import { useState } from "react";
import {Input} from "@nextui-org/input";
import {Button} from "@nextui-org/button";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import {Card, CardHeader, CardBody, CardFooter, Divider, Link} from "@nextui-org/react";
import {
    Popover,
    PopoverContent,
    PopoverTrigger,
  } from "@/components/ui/popover"
import { format, set } from "date-fns"
import { Calendar as CalendarIcon } from "lucide-react"
import { cn } from "@/lib/utils"
import { Calendar } from "@/components/ui/calendar"
import axios from "axios";

function AddTips() {
    const [declaredTips, setDeclaredTips] = useState("");
    const [cashTips, setCashTips] = useState("");
    const [foodSales, setFoodSales] = useState("");
    const [naBevSales, setNaBevSales] = useState("");
    const [alcoholSales, setAlcoholSales] = useState("");
    const [date, setDate] = useState("");
    
    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("Declared Tips: ", declaredTips);
        console.log("Cash Tips: ", cashTips);
        console.log("Food Sales: ", foodSales);
        console.log("N/A Bev Sales: ", naBevSales);
        console.log("Alcohol Sales: ", alcoholSales);
        console.log("Date: ", date);
        axios.post("http://localhost:5000/", {
            declaredTips: declaredTips,
            cashTips: cashTips,
            foodSales: foodSales,
            naBevSales: naBevSales,
            alcoholSales: alcoholSales,
            date: date
        })
        .then(response => response.json())
        then(data => {
            if (data.status === "success") {
                setMessage("Tips added successfully");
            } else {
                setMessage(data.message);
            }
        });
    }

    return (
        <>
        <Card className="flex justify-center items-center p-6 shadow-lg">
            <CardHeader className="flex gap-3 justify-center bg-gray-100 p-4 rounded-t-lg">
                <div className="flex flex-col">
                    <p className="text-lg font-semibold">Input Tips</p>
                </div>
            </CardHeader>
            <Divider/>
            <CardBody className="bg-gray-50 p-4 rounded-b-lg">
                <div className="flex w-full flex-wrap md:flex-nowrap gap-4 justify-center">
                    <Select>
                        <SelectTrigger className="w-[280px]">
                            <SelectValue placeholder="Select Job Class" />
                        </SelectTrigger>
                        <SelectContent>
                            <SelectItem value="bayhost">BayHost</SelectItem>
                            <SelectItem value="shiftlead">Shift Lead</SelectItem>
                            <SelectItem value="eventambassador">Event Ambassador</SelectItem>
                        </SelectContent>
                    </Select>
                </div>
            </CardBody>
            <CardBody className="bg-gray-50 p-4 rounded-b-lg">
                <div className="flex w-full flex-wrap md:flex-nowrap gap-4 justify-center">
                <Popover>
                    <PopoverTrigger asChild>
                        <Button
                        variant={"outline"}
                        className={cn(
                            "w-[280px] justify-center text-left font-normal",
                            !date && "text-muted-foreground"
                        )}
                        >
                        <CalendarIcon className="mr-2 h-4 w-4" />
                        {date ? format(date, "PPP") : <span>Pick a date</span>}
                        </Button>
                    </PopoverTrigger>
                    <PopoverContent className="w-auto p-0">
                        <Calendar
                        mode="single"
                        selected={date}
                        onSelect={setDate}
                        initialFocus
                        />
                    </PopoverContent>
                    </Popover>
                </div>
            </CardBody>
            
            <CardBody className="bg-gray-50 p-4 rounded-b-lg">
                <div className="flex w-full flex-wrap md:flex-nowrap gap-4 mb-4"> 
                    <Input type="text" label="Declared Tips" placeholder="Enter your Declared Tips" 
                        id="declaredTips"
                        value={declaredTips}
                        onChange={(e) => setDeclaredTips(e.target.value)}
                        />
                </div>
            </CardBody>
            <CardBody className="bg-gray-50 p-4 rounded-b-lg">
                <div className="flex w-full flex-wrap md:flex-nowrap gap-4 mb-4"> 
                    <Input type="text" label="Cash Tips" placeholder="Enter your Cash Tips" 
                        id="cashTips"
                        value={cashTips}
                        onChange={(e) => setCashTips(e.target.value)}/>
                </div>
            </CardBody>
            <Divider/>

            <CardHeader className="flex gap-3 justify-center bg-gray-100 p-4 rounded-t-lg">
                <div className="flex flex-col">
                    <p className="text-lg font-semibold">Tipout Numbers (Optional)</p>
                </div>
            </CardHeader>
            <CardBody className="bg-gray-50 p-4 rounded-b-lg">
                <div className="flex w-full flex-wrap md:flex-nowrap gap-4"> 
                    <Input type="text" label="Food Sales" placeholder="Enter your Food Sales" />
                </div>
            </CardBody>
            <CardBody className="bg-gray-50 p-4 rounded-b-lg">
                <div className="flex w-full flex-wrap md:flex-nowrap gap-4"> 
                    <Input type="text" label="N/A Bev Sales" placeholder="Enter your N/A Bev Sales" />
                </div>
            </CardBody>
            <CardBody className="bg-gray-50 p-4 rounded-b-lg">
                <div className="flex w-full flex-wrap md:flex-nowrap gap-4"> 
                    <Input type="text" label="Alcohol Sales" placeholder="Enter your Alcohol Sales" />
                </div>
            </CardBody>
            <CardFooter className="flex justify-center">
                <Button className="bg-slate-blueish" onClick={handleSubmit}>Submit</Button>
            </CardFooter>
        </Card>
        </>
    );
}
export default AddTips;
