module.exports = {
    devServer: {
      proxy: {
        '/api': {
          target: 'http://127.0.0.1:5000',  // Seu servidor Flask
          changeOrigin: true,
          pathRewrite: {
            '^/api': ''
          }
        }
      }
    }
  }