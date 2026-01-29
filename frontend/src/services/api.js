const BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export async function analyzeWebsite(payload) {
  const url = `${BASE.replace(/\/$/, '')}/analyze`
  console.log('analyzeWebsite POST ->', url, payload)

  // timeout support
  const controller = new AbortController()
  const TIMEOUT = 15000 // ms
  const timeoutId = setTimeout(() => controller.abort(), TIMEOUT)

  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
      signal: controller.signal,
    })
    clearTimeout(timeoutId)

    const text = await res.text()
    let data
    try {
      data = text ? JSON.parse(text) : null
    } catch (parseErr) {
      data = text
    }

    console.log('analyzeWebsite response status=', res.status, 'body=', data)

    if (!res.ok) {
      const msg = typeof data === 'string' ? data : (data && data.error) || JSON.stringify(data)
      throw new Error(`HTTP ${res.status} ${res.statusText}: ${msg}`)
    }

    return data
  } catch (err) {
    clearTimeout(timeoutId)
    if (err.name === 'AbortError') {
      console.error('analyzeWebsite error: request timed out')
      throw new Error('Request timed out')
    }
    console.error('analyzeWebsite error', err)
    throw err
  }
}
