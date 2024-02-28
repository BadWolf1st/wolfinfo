import React from 'react';
import ReactDOMClient from 'react-dom/client';
import Home from './pages/Home';


const elements = (
<Home/>
)

const app = ReactDOMClient.createRoot(document.getElementById('root'));

app.render(elements)
