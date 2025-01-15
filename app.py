from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    # Get form data
    data = request.form.get('data', '')  # Default to empty string
    size = int(request.form.get('size', 200))  # Default size
    border = int(request.form.get('border', 4))  # Default border size
    color = request.form.get('color', "#ffffff")  # Default background color

    if not data:
        return "Error: No data provided to generate QR code", 400

    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Use a fixed box size for clarity
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color=color)

    # Save image to BytesIO buffer
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='qrcode.png')

if __name__ == '__main__':
    app.run(debug=True)
