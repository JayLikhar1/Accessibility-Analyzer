import { useState } from 'react'

function AccessibilityChecklist({ checklist }) {
  const [expandedItems, setExpandedItems] = useState({})

  const toggleItem = (index) => {
    setExpandedItems(prev => ({
      ...prev,
      [index]: !prev[index]
    }))
  }

  const getStatusIcon = (status) => {
    if (status === 'pass') {
      return <span className="text-severity-low text-xl">✓</span>
    }
    return <span className="text-severity-high text-xl">✖</span>
  }

  const getSeverityBadge = (severity) => {
    const colors = {
      High: 'bg-red-100 text-red-800',
      Medium: 'bg-yellow-100 text-yellow-800',
      Low: 'bg-green-100 text-green-800'
    }
    return (
      <span className={`px-2 py-1 rounded text-xs font-medium ${colors[severity] || colors.Low}`}>
        {severity}
      </span>
    )
  }

  return (
    <div className="space-y-3">
      {checklist.map((item, index) => (
        <div
          key={index}
          className={`border border-border-color rounded-lg overflow-hidden ${
            item.status === 'fail' ? 'bg-red-50' : 'bg-white'
          }`}
        >
          <button
            onClick={() => toggleItem(index)}
            className="w-full px-4 py-4 flex items-center justify-between text-left hover:bg-gray-50 transition-colors focus:outline-none focus:ring-2 focus:ring-primary-cta"
            aria-expanded={expandedItems[index] || false}
          >
            <div className="flex items-center gap-4 flex-1">
              <div className="flex-shrink-0">
                {getStatusIcon(item.status)}
              </div>
              <div className="flex-1">
                <div className="flex items-center gap-3 mb-1">
                  <span className="font-medium text-text-primary">{item.check}</span>
                  {getSeverityBadge(item.severity)}
                  <span className="text-xs text-text-muted">WCAG {item.wcag}</span>
                </div>
                {item.total > 0 && (
                  <p className="text-sm text-text-muted">
                    {item.passed} passed, {item.failed} failed (out of {item.total})
                  </p>
                )}
              </div>
            </div>
            <div className="flex-shrink-0 ml-4">
              <span className="text-text-muted">
                {expandedItems[index] ? '▼' : '▶'}
              </span>
            </div>
          </button>
          
          {expandedItems[index] && (
            <div className="px-4 pb-4 pt-2 border-t border-border-color bg-white">
              <p className="text-sm text-text-muted mb-3">{item.description}</p>
              {item.status === 'fail' && (
                <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3">
                  <p className="text-sm font-medium text-text-primary mb-1">Fix Suggestion:</p>
                  <p className="text-sm text-text-muted">{item.fix}</p>
                </div>
              )}
            </div>
          )}
        </div>
      ))}
    </div>
  )
}

export default AccessibilityChecklist
