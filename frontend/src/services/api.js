// ✅ Prefer the correct Vercel env var, keep backward compatibility
const BASE =
  import.meta.env.VITE_API_BASE_URL ||
  import.meta.env.VITE_API_URL ||
  'http://localhost:8000'

// Normalize payload so backend always receives { url: string }
function normalizePayload(payload) {
  if (!payload) return {}
  if (typeof payload === 'string') return { url: payload.trim() }
  return payload
}

export async function analyzeWebsite(payload) {
  const bodyPayload = normalizePayload(payload)

  // 🚨 Guard: URL must exist
  if (!bodyPayload.url) {
    throw new Error('URL is required')
  }

  const url = `${BASE.replace(/\/$/, '')}/analyze`
  console.log('[analyzeWebsite] POST →', url, bodyPayload)

  // Timeout support
  const controller = new AbortController()
  const TIMEOUT = 30000 // 30s
  const timeoutId = setTimeout(() => controller.abort(), TIMEOUT)

  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify(bodyPayload),
      signal: controller.signal,
    })

    clearTimeout(timeoutId)

    // 204 No Content is valid
    if (res.status === 204) {
      console.warn('[analyzeWebsite] 204 No Content')
      return null
    }

    const text = await res.text()

    let data
    try {
      data = text ? JSON.parse(text) : null
    } catch {
      // Non-JSON response (still useful for debugging)
      data = text
    }

    console.log(
      '[analyzeWebsite] response',
      { status: res.status, body: data }
    )

    // ❌ Backend returned error
    if (!res.ok) {
      const message =
        typeof data === 'string'
          ? data
          : data?.error || data?.detail || data?.message || 'Analysis failed'

      const err = new Error(message)
      err.status = res.status
      err.body = data
      throw err
    }

    // ✅ Success
    return data

  } catch (err) {
    clearTimeout(timeoutId)

    if (err.name === 'AbortError') {
      console.error('[analyzeWebsite] timeout')
      throw new Error('Request timed out. Please try again.')
    }

    if (err instanceof TypeError) {
      console.error('[analyzeWebsite] network/CORS error:', err.message)
      throw new Error(
        `Network error: ${err.message}. Check backend URL and CORS configuration.`
      )
    }

    console.error('[analyzeWebsite] error:', err)
    throw err
  }
}
