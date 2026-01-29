const BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export async function analyzeWebsite(payload) {
  const url = `${BASE.replace(/\/$/, '')}/analyze`
  console.log('analyzeWebsite POST ->', url, payload)
  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    })
    const text = await res.text()
    console.log('analyzeWebsite response status=', res.status, 'body=', text)
    if (!res.ok) throw new Error(`HTTP ${res.status}: ${text}`)
    return JSON.parse(text)
  } catch (err) {
    console.error('analyzeWebsite error', err)
    throw err
  }
}
