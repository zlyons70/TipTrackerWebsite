// import React, { useState, useEffect } from 'react';
// import ReactDOM from 'react-dom/client';
// import Dashboard from './Dashboard';
// import { NextUIProvider } from '@nextui-org/react';
// import { useNavigate } from 'react-router-dom';
// import httpClient from '../../httpClient';


// const Home = () => {
//     const navigate = useNavigate();
//     const [user, setUser] = useState(null);

//     useEffect(() => {
//         (async () => {
//             try {
//                 const response = await httpClient.get('//localhost:5000/@me');
//                 setUser(response.data);
//                 console.log(response.data);
//             } catch (error) {
//                 console.log("not authenticated")
//                 navigate('/login');
//             }
//         })();
//     }, [navigate]);

//     return (
//         <React.StrictMode>
//             <NextUIProvider>
//                 {user != null ? <Dashboard /> : <Login />}
//             </NextUIProvider>
//         </React.StrictMode>
//     );
// };

// ReactDOM.createRoot(document.getElementById('root')).render(<Home />);