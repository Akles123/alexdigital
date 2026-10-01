from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>ALEX Digital</title>

<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f2f5f8;
    text-align: center;
}

.header {
    background: linear-gradient(135deg, #111827, #2563eb);
    color: white;
    padding: 45px 20px;
}

.logo {
    width: 90px;
    height: 90px;
    margin: auto;
    border-radius: 50%;
    background: white;
    color: #2563eb;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 35px;
    font-weight: bold;
}

h1 {
    margin-bottom: 5px;
}

.card {
    max-width: 500px;
    margin: 25px auto;
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.service {
    background: #eef4ff;
    padding: 15px;
    margin: 10px 0;
    border-radius: 12px;
}

.button {
    display: block;
    padding: 15px;
    margin-top: 12px;
    border-radius: 12px;
    text-decoration: none;
    color: white;
    font-weight: bold;
}

.call {
    background: #2563eb;
}

.whatsapp {
    background: #16a34a;
}

.maps {
    background: #dc2626;
}

.footer {
    padding: 20px;
    color: #666;
}
</style>
</head>

<body>

<div class="header">

<div class="logo">A</div>

<h1>ALEX Digital</h1>

<p>Your Digital Service Point</p>

</div>

<div class="card">

<h2>💻 हमारी Services</h2>

<div class="service">
📱 Digital Services
</div>

<div class="service">
🖥️ Online Services
</div>

<div class="service">
📄 Form & Document Services
</div>

<h2>📍 पता</h2>

<p>Shikaripara, Jharkhand</p>

<a class="button call" href="tel:9771871811">
📞 Call Now
</a>

<a class="button whatsapp"
href="https://wa.me/919771871811">
💬 WhatsApp
</a>

<a class="button maps"
href="https://www.google.com/maps/search/?api=1&query=Shikaripara,Jharkhand">
📍 Google Maps
</a>

</div>

<div class="footer">
© 2026 ALEX Digital
</div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
