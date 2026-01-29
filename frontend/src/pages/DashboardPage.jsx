import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import SummaryCards from '../components/SummaryCards'
import AccessibilityChecklist from '../components/AccessibilityChecklist'
import IssuesTable from '../components/IssuesTable'
import ScoreCard from '../components/ScoreCard'

function DashboardPage() {
  const [result, setResult] = useState(null)
  const navigate = useNavigate()

  useEffect(() => {
    // Get result from sessionStorage
    const storedResult = sessionStorage.getItem('analysisResult')
    if (storedResult) {
      setResult(JSON.parse(storedResult))
    } else {
      // Redirect if no result
      navigate('/')
    }
  }, [navigate])

  if (!result) {
    return (
      <div className="text-center py-12">
        <p className="text-text-muted">Loading...</p>
      </div>
    )
  }

  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-text-primary mb-2">
            Accessibility Report
          </h1>
          <p className="text-text-muted">{result.url}</p>
        </div>
        <button
          onClick={() => navigate('/')}
          className="btn-secondary"
        >
          Analyze Another
        </button>
      </div>

      {/* Overall Score */}
      <ScoreCard score={result.overall_score} />

      {/* Summary Cards */}
      <SummaryCards summary={result.summary} />

      {/* Accessibility Checklist */}
      <div className="card">
        <h2 className="text-2xl font-semibold text-text-primary mb-6">
          Accessibility Checklist
        </h2>
        <AccessibilityChecklist checklist={result.checklist} />
      </div>

      {/* Issues Table */}
      {result.issues && result.issues.length > 0 && (
        <div className="card">
          <h2 className="text-2xl font-semibold text-text-primary mb-6">
            Issues Found
          </h2>
          <IssuesTable issues={result.issues} />
        </div>
      )}

      {/* Metadata */}
      {result.metadata && (
        <div className="text-sm text-text-muted text-center">
          <p>Analyzed on {new Date(result.metadata.timestamp).toLocaleString()}</p>
          {result.metadata.title && <p>Page: {result.metadata.title}</p>}
        </div>
      )}
    </div>
  )
}

export default DashboardPage
