const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 600,
    height: 600,
    resizable: false,
    transparent: true,
    frame: false,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js'),
      devTools: false
    },
    icon: path.join(__dirname, 'icon.ico')
  });

  win.webContents.on('before-input-event', (event, input) => {
    if (input.control && input.shift && (input.key.toLowerCase() === 'i' || input.key.toLowerCase() === 'j')) {
      event.preventDefault();
    }
  });

  win.loadFile('index.html');
  win.setMenuBarVisibility(false);
}

app.whenReady().then(() => {
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

ipcMain.on('window-control', (event, action) => {
  const win = BrowserWindow.getFocusedWindow();
  if (!win) return;
  if (action === 'minimize') win.minimize();
  else if (action === 'maximize') win.isMaximized() ? win.unmaximize() : win.maximize();
  else if (action === 'close') win.close();
});

ipcMain.handle('get-gpu-version', async () => {
  const { getGpuVersion } = require('./local_version');
  return await getGpuVersion();
});

ipcMain.handle('get-latest-version', async () => {
  const { getLatestVersion } = require('./latest_version');
  return await getLatestVersion();
});

ipcMain.handle('open-external', async (event, url) => {
  const { shell } = require('electron');
  await shell.openExternal(url);
});

ipcMain.handle('quit-app', () => {
  app.quit();
}); 