const { exec } = require('child_process');
function executeWmicCommand(command) {
    return new Promise((resolve, reject) => {
        exec(`wmic ${command}`, { encoding: 'utf8' }, (error, stdout, stderr) => {
            if (error) {
                reject(error);
                return;
            }
            if (stderr) {
                reject(new Error(stderr));
                return;
            }
            resolve(stdout);
        });
    });
}

async function checkGpuDrivers() {
    try {
        const gpuOutput = await executeWmicCommand('path win32_videocontroller get Name,DriverVersion /format:csv');
        return gpuOutput;
    } catch (error) {
        console.error('Error executing WMIC command:', error.message);
    }
}

async function getGpuVersion() {
    const gpuOutput = await checkGpuDrivers();
    const lines = gpuOutput.trim().split('\n');
    lines.shift();
    const gpuInfo = [];
    for (const line of lines) {
        const [_, version, name] = line.split(',');
        gpuInfo.push({ version, name });
    }

    const nvidiaGpu = gpuInfo.find(gpu => gpu.name.includes('NVIDIA'));
    const versionNumber = nvidiaGpu.version.replace(/\./g, '').slice(-5);
    console.log("local version:",versionNumber);
    return versionNumber;
}

module.exports = {
    getGpuVersion
};