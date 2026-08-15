from flask import Flask, render_template, request, redirect, session, url_for
#from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import os
import smtplib
import mimetypes
from email.message import EmailMessage
from werkzeug.utils import secure_filename

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SESSION_SECRET")
#oauth = OAuth(app)

UPLOAD_FOLDER = '/tmp/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#microsoft = oauth.register(
#    name='microsoft',
#    client_id=os.getenv('CLIENT_ID'),
#    client_secret=os.getenv('CLIENT_SECRET'),
#    server_metadata_url=f"{os.getenv('AUTHORITY')}/v2.0/.well-known/openid-configuration",
#    client_kwargs={'scope': os.getenv("SCOPE")},
#)

@app.route('/')
def home():
#    user = session.get('user')
#    if user:
     return redirect('/form')
#    return redirect('/login')

#@app.route('/login')
#def login():
#    return microsoft.authorize_redirect(redirect_uri=os.getenv("REDIRECT_URI"))

#@app.route('/auth/callback')
#def auth_callback():
#    token = microsoft.authorize_access_token()
#    user_info = token.get('userinfo')
#    session['user'] = {
#        'name': user_info['name'],
#        'email': user_info['preferred_username']
#    }
#    return redirect('/form')

#@app.route('/logout')
#def logout():
#    session.pop('user', None)
#    return redirect('/')

@app.route('/form', methods=['GET', 'POST'])
def form():
    #if 'user' not in session:
    #    return redirect('/')

    if request.method == 'POST':
        # Get form data
        sales_rep_name = request.form.get('sales_rep_name')
        customer_name = request.form.get('customer_name')
        item = request.form.get('item')
        logo_available = request.form.get('logo_available')
        logo_location = request.form.get('logo_location')
        supplier = request.form.get('supplier')
        usage = request.form.get('usage')
        cost = request.form.get('cost')
        order_type = request.form.get('order_type')
        comments = request.form.get('comments')
       

         # Handle logo file
        logo_file = request.files.get('logo_file')
        filename = None
        if logo_file and logo_available == 'yes':
            filename = secure_filename(logo_file.filename)
            if filename.endswith(('.ai', '.eps', '.pdf', '.svg')):
                logo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                logo_file.save(logo_path)
            else:
                return "Invalid file format for logo. Acceptable: .ai, .eps, .pdf, .svg", 400

        # Email setup
        msg = EmailMessage()
        msg['Subject'] = 'New Custom Request Submission'
        msg['From'] = os.getenv('EMAIL_HOST_USER')
        msg['To'] = os.getenv('EMAIL_RECEIVER')

        msg.set_content(f"""
Sales Rep: {sales_rep_name}
Customer Name: {customer_name}
Item: {item}
Logo Available: {logo_available}
Desired Logo Location: {logo_location}
Preferred Supplier: {supplier}
Monthly Usage: {usage}
Target Cost: {cost}
Order Type: {order_type}
Additional Comments: {comments}
        """)

        # Attach logo if applicable
        if logo_file and filename:
            with open(logo_path, 'rb') as f:
                msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename=filename)

        # Send email via Microsoft Exchange SMTP
        with smtplib.SMTP('smtp.office365.com', 587) as smtp:
            smtp.starttls()
            smtp.login(os.getenv('EMAIL_HOST_USER'), os.getenv('EMAIL_HOST_PASSWORD'))
            smtp.send_message(msg)

        return redirect('/thankyou')

    return render_template('form.html')

@app.route('/thankyou')
def thankyou():
    return "Thank you for submitting the form."

#def send_email(responses, file_path):
#    msg = EmailMessage()
#    msg['Subject'] = f"New Custom Request Submission"
#    msg['From'] = os.getenv("EMAIL_HOST_USER")
#    msg['To'] = os.getenv("EMAIL_RECEIVER")

#    content = f"Custom item request form:\n\n"
#    for k, v in responses.items():
#        content += f"{k}: {v}\n"
#    msg.set_content(content)

#    if file_path:
#        mime_type, _ = mimetypes.guess_type(file_path)
#        maintype, subtype = mime_type.split('/', 1)
#        with open(file_path, 'rb') as f:
#            msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=os.path.basename(file_path))

#   with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as server:
#        server.starttls()
#        server.login(os.getenv("SMTP_USERNAME"), os.getenv("SMTP_PASSWORD"))
#        server.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True)
