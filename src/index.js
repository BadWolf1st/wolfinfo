import React from 'react';
import ReactDOMClient from 'react-dom/client';
import Home from './pages/Home';

// Дорогой программист:
// Когда я писал этот код, только бог и
// я знали как он работает.
// Теперь это знает только бог!
// Тем не менее, если ты попытаешься соптимизировать
// этот сайт и обосрешься (что скорей всего),
// прошу, увеличь этот счетчик как
// предупреждение для своих последователей:
// количество_впустую_потраченных_часов = 4

// Our Father, Who art in the Heavens, hallowed be Thy name.
// Thy kingdom come, Thy will be done, on earth as it is in heaven.
// Give us this day our daily bread, and forgive us our debts, 
// as we forgive our debtors; and lead us not into temptation, but deliver us from the evil one.

const elements = (
<Home/>
)

const app = ReactDOMClient.createRoot(document.getElementById('root'));

app.render(elements)
