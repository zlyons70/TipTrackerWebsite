import React, { useState, useEffect } from "react";
import Calendar from "react-calendar";
import 'react-calendar/dist/Calendar.css'; // Calendar styling
import httpClient from "../../httpClient";

const sampleData = {
  "2024-10-24": { hoursWorked: 8, netEarnings: 150 },
  "2024-10-25": { hoursWorked: 6, netEarnings: 120 },
  // Add more entries here
};

const TipCalendar = ({ user }) => {
    const [date, setDate] = useState(new Date());
    const [tileData, setTileData] = useState({});
    const getTileContent = ({ date, view }) => {
        const formattedDate = date.toISOString().split('T')[0];

        if (view === "month" && sampleData[formattedDate]) {
            const { hoursWorked, netEarnings } = sampleData[formattedDate];
            return (
            <div>
                <p>{hoursWorked} hrs</p>
                <p>${netEarnings}</p>
            </div>
            );
     }
        return null;
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
    } catch (error) {
        console.log("Failed to get tips");
    }
}
export default TipCalendar;