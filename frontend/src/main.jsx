import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './styles/index.css'

// debug: show the VITE API URL baked into the build
console.log('VITE_API_URL =', import.meta.env.VITE_API_URL)

// catch unhandled rejections so fetch errors show in console
window.addEventListener('unhandledrejection', event => {
  console.error('Unhandled promise rejection:', event.reason)
})

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)

