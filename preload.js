const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  getGpuVersion: () => ipcRenderer.invoke('get-gpu-version'),
  getLatestVersion: () => ipcRenderer.invoke('get-latest-version'),
  openExternal: (url) => ipcRenderer.invoke('open-external', url),
  quitApp: () => ipcRenderer.invoke('quit-app'),
  windowControl: (action) => ipcRenderer.send('window-control', action)
}); 