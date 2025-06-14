document.getElementById('checkUpdate').addEventListener('click', () => {
    const downloadButton = document.getElementById('downloadButton');
    downloadButton.style.display = downloadButton.style.display === 'none' ? 'block' : 'none';
});

document.getElementById('downloadButton').addEventListener('click', () => {
    console.log('Download clicked');
}); 