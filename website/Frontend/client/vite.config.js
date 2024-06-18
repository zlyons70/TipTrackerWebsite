import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'
// https://vitejs.dev/config/
const root = resolve(__dirname, 'src')
const outDir = resolve(__dirname, 'dist')

export default defineConfig({
  root,
  plugins: [react()],
  build: {
    outDir,
    emptyOutDir: true,
    // specifies the entry points for the build
    rollupOptions: {
      input: {
        main: resolve(root, 'index.html'),
        home: resolve(root,'home', 'index.html'),
      }
  }
}
})
