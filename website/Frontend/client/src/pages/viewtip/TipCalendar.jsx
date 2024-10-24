import React, { useState } from "react";
import Calendar from "react-calendar";
import 'react-calendar/dist/Calendar.css'; // Calendar styling

const sampleData = {
  "2024-10-24": { hoursWorked: 8, netEarnings: 150 },
  "2024-10-25": { hoursWorked: 6, netEarnings: 120 },
  // Add more entries here
};

const TipCalendar = () => {
  const [date, setDate] = useState(new Date());

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

export default TipCalendar;