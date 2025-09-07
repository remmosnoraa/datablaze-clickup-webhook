from http.server import BaseHTTPRequestHandler
import json
import urllib.request
import urllib.parse
import os

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Read webhook data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            webhook_data = json.loads(post_data.decode('utf-8'))
            
            # Only process new rows
            if webhook_data.get('event_type') == 'rows.created' and webhook_data.get('items'):
                client = webhook_data['items'][0]
                
                # Handle null values properly
                first_name = (client.get('First Name') or '').strip()
                last_name = (client.get('Last Name') or '').strip()
                task_name = f"{first_name} {last_name}".strip()
                
                # Don't create tasks for empty names
                if task_name:
                    url = "https://api.clickup.com/api/v2/list/901102682453/task"
                    
                    data = {
                        "name": task_name,
                        "description": f"Email: {client.get('Email') or ''}\nPhone: {client.get('Phone #') or ''}"
                    }
                    
                    req = urllib.request.Request(
                        url,
                        data=json.dumps(data).encode('utf-8'),
                        headers={
                            'Authorization': os.environ.get('CLICKUP_TOKEN'),
                            'Content-Type': 'application/json'
                        }
                    )
                    
                    urllib.request.urlopen(req)
            
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f'Error: {str(e)}'.encode())
