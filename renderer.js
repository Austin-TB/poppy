document.getElementById('checkUpdate').addEventListener('click', async () => {
    const checkBtn = document.getElementById('checkUpdate');
    const loader = document.getElementById('loader');
    const downloadBtn = document.getElementById('downloadButton');
    const currentVersionElement = document.getElementById('currentVersion');
    const latestVersionElement = document.getElementById('latestVersion');

    currentVersionElement.style.visibility = 'hidden';
    latestVersionElement.style.visibility = 'hidden';
    loader.style.display = 'block';
    checkBtn.disabled = true;

    try {
        const localVersionNumber = await window.electronAPI.getGpuVersion();
        const localVersion = `${localVersionNumber.slice(0, 3)}.${localVersionNumber.slice(3, 5)}`;
        const latestVersionNumber = await window.electronAPI.getLatestVersion();
        const latestVersion = `${latestVersionNumber.slice(0, 3)}.${latestVersionNumber.slice(3, 5)}`;
        const updateAvailable = parseInt(localVersionNumber) < parseInt(latestVersionNumber);

        if (updateAvailable) {
            downloadBtn.style.display = 'block';
            downloadBtn.onclick = () => {
                window.electronAPI.openExternal(`https://us.download.nvidia.com/Windows/${latestVersion}/${latestVersion}-notebook-win10-win11-64bit-international-dch-whql.exe`);
                window.electronAPI.quitApp();
            };
        } else {
            downloadBtn.style.display = 'none';
        }

        currentVersionElement.textContent = `Current Driver Version: ${localVersion}`;
        latestVersionElement.textContent = `Latest Driver Version: ${latestVersion}`;
    } catch (err) {
        currentVersionElement.textContent = 'Error fetching version info.';
        latestVersionElement.textContent = '';
    } finally {
        loader.style.display = 'none';
        currentVersionElement.style.visibility = 'visible';
        latestVersionElement.style.visibility = 'visible';
        checkBtn.disabled = false;
    }
});

window.onload = () => {
    document.getElementById('downloadButton').style.display = 'none';
};

window.addEventListener('DOMContentLoaded', () => {
    document.getElementById('min-btn').onclick = () => window.electronAPI.windowControl('minimize');
    document.getElementById('close-btn').onclick = () => window.electronAPI.windowControl('close');
});
