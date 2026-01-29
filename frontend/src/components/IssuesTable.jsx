function IssuesTable({ issues }) {
  const getSeverityColor = (severity) => {
    const colors = {
      High: 'text-severity-high bg-red-50 border-red-200',
      Medium: 'text-severity-medium bg-yellow-50 border-yellow-200',
      Low: 'text-severity-low bg-green-50 border-green-200'
    }
    return colors[severity] || colors.Low
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full border-collapse">
        <thead>
          <tr className="border-b border-border-color">
            <th className="text-left py-3 px-4 font-semibold text-text-primary">Issue</th>
            <th className="text-left py-3 px-4 font-semibold text-text-primary">WCAG</th>
            <th className="text-left py-3 px-4 font-semibold text-text-primary">Severity</th>
            <th className="text-left py-3 px-4 font-semibold text-text-primary">Count</th>
            <th className="text-left py-3 px-4 font-semibold text-text-primary">Fix</th>
          </tr>
        </thead>
        <tbody>
          {issues.map((issue, index) => (
            <tr
              key={index}
              className="border-b border-border-color hover:bg-gray-50 transition-colors"
            >
              <td className="py-3 px-4 text-text-primary">{issue.check}</td>
              <td className="py-3 px-4 text-text-muted text-sm">{issue.wcag}</td>
              <td className="py-3 px-4">
                <span className={`px-2 py-1 rounded text-xs font-medium border ${getSeverityColor(issue.severity)}`}>
                  {issue.severity}
                </span>
              </td>
              <td className="py-3 px-4 text-text-primary">{issue.count || 0}</td>
              <td className="py-3 px-4 text-sm text-text-muted max-w-md">{issue.fix}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default IssuesTable
