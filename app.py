from flask import Flask, render_template
import os
import datetime
import pytz
import subprocess

app = Flask(__name__)

def get_top_output():
    try:
        # Run the top command in batch mode (-b) and get one iteration (-n 1)
        result = subprocess.run(['top', '-b', '-n', '1'], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error getting top output: {str(e)}"

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv('USER', os.getenv('USERNAME', 'unknown'))
    
    # Get current time in IST
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %z')
    
    # Get top command output
    top_output = get_top_output()
    
    return f"""
    <pre>
Name: [Nikhil Kumar Saini]
User: {username}
Server Time (IST): {current_time}
TOP output:
{top_output}
    </pre>
    """

if __name__ == '__main__':
    # Run on port 5000 by default
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)