import React, { useState, useEffect } from "react";
import Calendar from "react-calendar";
import 'react-calendar/dist/Calendar.css'; // Calendar styling
import httpClient from "../../httpClient";
import { set } from "date-fns";
import { Item } from "@radix-ui/react-dropdown-menu";

const sampleData = {
  "2024-10-24": { hoursWorked: 8, netEarnings: 150 },
  "2024-10-25": { hoursWorked: 6, netEarnings: 120 },
  // Add more entries here
};

const TipCalendar = ({ user }) => {
    const [date, setDate] = useState(new Date());
    const [tileData, setTileData] = useState({});

    useEffect(() => {
        getTips(user, date);
    }, [user, date]);

    const getTileContent = ({ date, view }) => {
        const formattedDate = date.toISOString().split('T')[0];
        if (view === "month" && tileData[formattedDate]) {
            const { gross } = tileData[formattedDate];
            return (
            <div>
                <p>${gross}</p>
            </div>
            );
     }
        return null;
    };

    const getTips = async (user, date) => {
        console.log("User: ", user);
        console.log("Date: ", date);
        date = date.toISOString().split('T')[0];
        console.log("Date: ", date);
        try {
            const response = await httpClient.post("http://localhost:5000/viewtips", 
                {
                    username: user,
                    date: date,
                    time: "month"
                }
            );
            console.log(response.data);
            // TODO NEED TO SET THE TILE DATA PROPERLY
        } catch (error) {
            console.log("Failed to get Tips");
        }
    };
    return (
    <div>
        <Calendar
        onChange={setDate}
        value={date}
        tileContent={getTileContent}
        />
    </div>
    );
    };
export default TipCalendar;