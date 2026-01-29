import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export const analyzeWebsite = async (url) => {
  try {
    const response = await api.post('/analyze', { url })
    return response.data
  } catch (error) {
    throw error
  }
}

export default api
