function SummaryCards({ summary }) {
  const cards = [
    {
      label: 'High Issues',
      value: summary.high_issues,
      color: 'text-severity-high',
      bgColor: 'bg-red-50',
      borderColor: 'border-red-200'
    },
    {
      label: 'Medium Issues',
      value: summary.medium_issues,
      color: 'text-severity-medium',
      bgColor: 'bg-yellow-50',
      borderColor: 'border-yellow-200'
    },
    {
      label: 'Low Issues',
      value: summary.low_issues,
      color: 'text-severity-low',
      bgColor: 'bg-green-50',
      borderColor: 'border-green-200'
    },
    {
      label: 'Checks Passed',
      value: `${summary.passed} / ${summary.total_checks}`,
      color: 'text-text-primary',
      bgColor: 'bg-blue-50',
      borderColor: 'border-blue-200'
    }
  ]

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
      {cards.map((card, index) => (
        <div
          key={index}
          className={`${card.bgColor} border ${card.borderColor} rounded-lg p-6`}
        >
          <p className="text-sm text-text-muted mb-2">{card.label}</p>
          <p className={`text-3xl font-bold ${card.color}`}>{card.value}</p>
        </div>
      ))}
    </div>
  )
}

export default SummaryCards
