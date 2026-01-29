function ScoreCard({ score }) {
  const getScoreColor = (score) => {
    if (score >= 80) return 'text-severity-low'
    if (score >= 60) return 'text-severity-medium'
    return 'text-severity-high'
  }

  const getScoreLabel = (score) => {
    if (score >= 80) return 'Excellent'
    if (score >= 60) return 'Good'
    if (score >= 40) return 'Needs Improvement'
    return 'Poor'
  }

  return (
    <div className="card text-center">
      <div className="mb-4">
        <p className="text-sm text-text-muted mb-2">Overall Accessibility Score</p>
        <div className={`text-6xl font-bold ${getScoreColor(score)} mb-2`}>
          {score}
        </div>
        <p className={`text-lg font-semibold ${getScoreColor(score)}`}>
          {getScoreLabel(score)}
        </p>
      </div>
      <div className="w-full bg-gray-200 rounded-full h-3">
        <div
          className={`h-3 rounded-full transition-all ${
            score >= 80 ? 'bg-severity-low' :
            score >= 60 ? 'bg-severity-medium' :
            'bg-severity-high'
          }`}
          style={{ width: `${score}%` }}
          role="progressbar"
          aria-valuenow={score}
          aria-valuemin="0"
          aria-valuemax="100"
        />
      </div>
    </div>
  )
}

export default ScoreCard
