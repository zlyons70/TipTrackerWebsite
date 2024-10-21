import React, { useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import Dashboard from './Dashboard';
import { NextUIProvider } from '@nextui-org/react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const Home = () => {
    const navigate = useNavigate();

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (!token) {
            navigate('/login'); // Redirect to login page if token is not present
        } else {
            // Send token to backend
            axios.get('http://localhost:5000/verify-token', {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            })
            .then(response => {
                if (response.data.status !== 'success') {
                    navigate('/login'); // Redirect to login if token is invalid
                }
            })
            .catch(error => {
                console.error('Error verifying token:', error);
                navigate('/login'); // Redirect to login on error
            });
        }
    }, [navigate]);

    return (
        <React.StrictMode>
            <NextUIProvider>
                <Dashboard />
            </NextUIProvider>
        </React.StrictMode>
    );
};

ReactDOM.createRoot(document.getElementById('root')).render(<Home />);