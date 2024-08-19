function runScraper(scraperUrl) {
    const loadingOverlay = document.getElementById('loading-overlay');
    // Mostrar la capa de carga
    loadingOverlay.style.display = 'flex';

    fetch(scraperUrl, {
        method: 'GET'
    })
    .then(response => {
        // Ocultar la capa de carga
        loadingOverlay.style.display = 'none';

        if (response.status === 403) {
            return response.text().then(message => showToast(message, 'warning'));
        } else if (response.ok) {
            return response.text().then(message => showToast(message, 'success'));
        } else {
            throw new Error('Unexpected response status: ' + response.status);
        }
    })
    .catch(error => {
        // Ocultar la capa de carga
        loadingOverlay.style.display = 'none';
        showToast('Error running scraper: ' + error, 'error');
    });
}

function showToast(message, type) {
    const toastContainer = document.querySelector('.toast-container');
    const toast = document.createElement('div');
    toast.className = `toast align-items-center ${type === 'success' ? 'toast-success' : type === 'warning' ? 'toast-warning' : 'text-bg-danger'} border-0`;
    toast.role = 'alert';
    toast.ariaLive = 'assertive';
    toast.ariaAtomic = 'true';
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${type === 'success' ? '✔ ' : ''}${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;
    toastContainer.appendChild(toast);
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();

    toast.addEventListener('hidden.bs.toast', () => {
        toast.remove();
    });
}

function showDetails(scraperName) {
    alert(`Details about the ${scraperName} scraper will be displayed here.`);
}