/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", "./static/**/*.js",
    './/templates/**/*.html',
  ],
  theme: {
    extend: {
		fontFamily: {
			poppins: ['Poppins', 'sans-serif'],
			roboto: ['Roboto', 'sans-serif'],
		},
		colors: {
			'buzzorange': '#f15a24',
		}
	},
  },
  plugins: [],
}
