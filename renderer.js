const { getGpuVersion } = require('./local_version');
const { getLatestVersion } = require('./latest_version');
const { shell, app } = require('electron');

document.getElementById('checkUpdate').addEventListener('click', async () => {
    const localVersionNumber = await getGpuVersion();
    const localVersion = `${localVersionNumber.slice(0, 3)}.${localVersionNumber.slice(3, 5)}`;
    console.log("local version:",localVersion);

    const latestVersionNumber = await getLatestVersion();
    const latestVersion = `${latestVersionNumber.slice(0, 3)}.${latestVersionNumber.slice(3, 5)}`;
    console.log("latest version:",latestVersion);

    const updateAvailable = parseInt(localVersionNumber) < parseInt(latestVersionNumber);
    if (updateAvailable) {
        document.getElementById('downloadButton').style.display = 'block';
        document.getElementById('downloadButton').addEventListener('click', () => {
            shell.openExternal(`https://us.download.nvidia.com/Windows/${latestVersion}/${latestVersion}-notebook-win10-win11-64bit-international-dch-whql.exe`);
            app.quit();
        });
    }

    const currentVersionElement = document.getElementById('currentVersion');
    const latestVersionElement = document.getElementById('latestVersion');
    
    currentVersionElement.textContent = `Current Driver Version: ${localVersion}`;
    latestVersionElement.textContent = `Latest Driver Version: ${latestVersion}`;
    currentVersionElement.style.display = 'block';
    latestVersionElement.style.display = 'block';
});
