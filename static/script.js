const form = document.getElementById('qrForm');
const qrCodeContainer = document.getElementById('qrcode');

form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form values
    const data = document.getElementById('data').value;
    const size = parseInt(document.getElementById('size').value);
    const border = document.getElementById('border').value;
    const color = document.getElementById('color').value;

    // Clear any previous QR Code
    qrCodeContainer.innerHTML = '';

    // Generate QR Code
    const qrCode = new QRCode(qrCodeContainer, {
        text: data,
        width: size,
        height: size,
        colorDark: "#000000",
        colorLight: color || "#ffffff",
    });

    // Apply custom border if specified
    if (border) {
        qrCodeContainer.style.padding = `${border}px`;
    } else {
        qrCodeContainer.style.padding = '0';
    }
});
