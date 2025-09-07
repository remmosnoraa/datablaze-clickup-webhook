#test
from http.server import BaseHTTPRequestHandler
import json
import requests
import os

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Get the webhook data from DataBlaze
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        webhook_data = json.loads(post_data.decode('utf-8'))
        
        # Extract client info from the webhook
        if webhook_data.get('event_type') == 'rows.created' and webhook_data.get('items'):
            client = webhook_data['items'][0]
            
            # Build task name
            first_name = client.get('First Name', '').strip()
            last_name = client.get('Last Name', '').strip()
            task_name = f"{first_name} {last_name}".strip()
            
            if task_name:
                # Create ClickUp task
                clickup_url = "https://api.clickup.com/api/v2/list/901102682453/task"
                
                headers = {
                    "Authorization": os.environ.get('CLICKUP_TOKEN'),
                    "Content-Type": "application/json"
                }
                
                task_data = {
                    "name": task_name,
                    "description": f"Email: {client.get('Email', '')}\nPhone: {client.get('Phone #', '')}\nLS Email: {client.get('LS Email', '')}"
                }
                
                response = requests.post(clickup_url, headers=headers, json=task_data)
        
        # Send response back to DataBlaze
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')
