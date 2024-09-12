const path = require('path');

module.exports = {
  entry: './src/index.js',  // Entry point of your JavaScript code
  output: {
    path: path.resolve(__dirname, 'dist'), // Output directory
    filename: 'main.js',  // Output bundle file
  },
  mode: 'development',  // You can switch to 'production' for production builds
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',  // Transpile modern JavaScript to compatible versions
          options: {
            presets: ['@babel/preset-env'],
          },
        },
      },
    ],
  },
  watch: true,  // Enable watching for changes
};