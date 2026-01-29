/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'bg-primary': '#F7F8FA',
        'card-bg': '#FFFFFF',
        'border-color': '#E5E7EB',
        'text-primary': '#111827',
        'text-muted': '#6B7280',
        'severity-high': '#DC2626',
        'severity-medium': '#F59E0B',
        'severity-low': '#16A34A',
        'primary-cta': '#2563EB',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
