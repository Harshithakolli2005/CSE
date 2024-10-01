# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message

app = Flask(__name__)
CORS(app)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME' ]='meenakshikatamneni@gmail.com'
app.config['MAIL PASSWORD']='meenakshi2708'
app.config['MAIL_DEFAULT_SENDER'] ='meenakshikatamneni@gmail.com'

mail = Mail(app)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    animal = data.get('animal')

    msg = Message('Animal Detected!', recipients=['harshithakkolliharshitha.com'])
    msg.body = f'An animal has been detected: {animal}'

    try:
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
