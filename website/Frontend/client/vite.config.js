import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'
import { log } from 'console'
import path from "path"
import { sign } from 'crypto'
// https://vitejs.dev/config/
const root = resolve(__dirname, 'src')
const pageRoot = resolve(__dirname, 'src/pages')
const outDir = resolve(__dirname, 'dist')

export default defineConfig({
  root,
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  build: {
    outDir,
    emptyOutDir: true,
    // specifies the entry points for the build
    rollupOptions: {
      input: {
        main: resolve(root, 'index.html'),
        home: resolve(root, 'pages/home/index.html'),
        login: resolve(root, 'pages/login/index.html'),
        signup: resolve(root, 'pages/signup/index.html'),
      }
  }
}
})
