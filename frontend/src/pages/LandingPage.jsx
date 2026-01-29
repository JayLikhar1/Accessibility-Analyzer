import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { analyzeWebsite } from '../services/api'

function LandingPage() {
  const [url, setUrl] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      const result = await analyzeWebsite(url)
      // Store result in sessionStorage for dashboard
      sessionStorage.setItem('analysisResult', JSON.stringify(result))
      navigate('/dashboard')
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to analyze website. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-4xl mx-auto">
      {/* Hero Section */}
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-text-primary mb-4">
          Accessibility Analyzer
        </h1>
        <p className="text-xl text-text-muted mb-8">
          Make your website usable for everyone.
        </p>
        <p className="text-base text-text-muted max-w-2xl mx-auto">
          Scan any website URL and get an actionable WCAG-based accessibility report 
          with checklist progress, issue severity, and clear fixes.
        </p>
      </div>

      {/* Analyzer Card */}
      <div className="card">
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="url" className="block text-sm font-medium text-text-primary mb-2">
              Website URL
            </label>
            <div className="flex gap-3">
              <input
                id="url"
                type="url"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="https://example.com"
                className="input-field flex-1"
                required
                disabled={loading}
                aria-label="Website URL input"
              />
              <button
                type="submit"
                className="btn-primary whitespace-nowrap"
                disabled={loading}
                aria-label="Analyze website"
              >
                {loading ? 'Analyzing...' : 'Analyze'}
              </button>
            </div>
          </div>
          
          {error && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-4">
              <p className="text-sm text-red-800">{error}</p>
            </div>
          )}
        </form>
      </div>

      {/* Features */}
      <div className="grid md:grid-cols-3 gap-6 mt-12">
        <div className="card text-center">
          <div className="text-3xl mb-3">✓</div>
          <h3 className="font-semibold text-text-primary mb-2">WCAG 2.1 Compliant</h3>
          <p className="text-sm text-text-muted">
            Comprehensive checks based on WCAG 2.1 guidelines
          </p>
        </div>
        <div className="card text-center">
          <div className="text-3xl mb-3">📊</div>
          <h3 className="font-semibold text-text-primary mb-2">Actionable Reports</h3>
          <p className="text-sm text-text-muted">
            Get clear fixes and prioritized issue lists
          </p>
        </div>
        <div className="card text-center">
          <div className="text-3xl mb-3">🤖</div>
          <h3 className="font-semibold text-text-primary mb-2">AI-Powered</h3>
          <p className="text-sm text-text-muted">
            ML-enhanced analysis for better accuracy
          </p>
        </div>
      </div>
    </div>
  )
}

export default LandingPage
