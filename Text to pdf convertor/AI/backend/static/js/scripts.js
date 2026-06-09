document.querySelector('form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const response = await fetch('/generate', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    if (data.html) {
        document.getElementById('preview').srcdoc = data.html;
    } else {
        alert('Error: ' + (data.error || 'Unknown error occurred.'));
    }
});