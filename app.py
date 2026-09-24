from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AWS Demo Dashboard</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f7fc;
                margin: 0;
                padding: 0;
            }
            header {
                background: #232f3e;
                color: white;
                padding: 20px;
                text-align: center;
            }
            .container {
                max-width: 1000px;
                margin: 30px auto;
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 20px;
            }
            .card {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                text-align: center;
            }
            .card h2 {
                color: #232f3e;
                margin: 0;
            }
            .value {
                font-size: 32px;
                color: #ff9900;
                font-weight: bold;
            }
            footer {
                text-align: center;
                padding: 20px;
                color: gray;
            }
        </style>
    </head>
    <body>

        <header>
            <h1>☁ AWS Cargill Dashboard</h1>
            <p>Successfully Hosted on EC2 Ubuntu Server</p>
        </header>

        <div class="container">
            <div class="card">
                <h2>Total Employees</h2>
                <p class="value">125</p>
            </div>

            <div class="card">
                <h2>Active Projects</h2>
                <p class="value">18</p>
            </div>

            <div class="card">
                <h2>Servers Running</h2>
                <p class="value">12</p>
            </div>

            <div class="card">
                <h2>AWS Region</h2>
                <p class="value">ap-south-1</p>
            </div>

            <div class="card">
                <h2>Environment</h2>
                <p class="value">Dev</p>
            </div>

            <div class="card">
                <h2>Status</h2>
                <p class="value">✅ Healthy</p>
            </div>
        </div>

        <footer>
            Demo Application Hosted on AWS EC2 using Flask
        </footer>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6162)
