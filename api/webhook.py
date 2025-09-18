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
            
            # Only process row updates
            if webhook_data.get('event_type') == 'rows.updated' and webhook_data.get('items'):
                client = webhook_data['items'][0]
                
                # Only create task if "Add to Clickup" is checked
                if client.get('Add to Clickup') == True:
                    # Handle null values properly
                    first_name = (client.get('First Name') or '').strip()
                    last_name = (client.get('Last Name') or '').strip()
                    task_name = f"{first_name} {last_name}".strip()
                    phone = ''.join(filter(str.isdigit, client.get('Phone #') or ''))
                    formatted_phone = f"+1 {phone[:3]} {phone[3:6]} {phone[6:]}" if len(phone) == 10 else phone
                    
                    if task_name:
                        url = "https://api.clickup.com/api/v2/list/901102682453/task"
                        
                        data = {
                            "name": task_name,
                            "description": client.get('Assignment Description') or '', # Assignment Description
                            "custom_fields": [
                                {
                                    "id": "cc2c56d8-5bd6-47c3-ae15-b53e1b4d186d",  # First Name
                                    "value": first_name  
                                },
                                {
                                    "id": "6bddcd8d-3d19-4ed1-8159-8f7a47ea5ed1",  # Last Name
                                    "value": last_name  
                                },                                
                                {
                                    "id": "eff6a583-46d3-4da6-8bca-a6a183b528fa",  # LS File
                                    "value": client.get('LS File') or ''
                                },
                                {
                                    "id": "1c22edaa-ee48-46cd-8db1-a42b470aabb5",  # Phone #
                                    "value": formatted_phone
                                },
                                {
                                    "id": "937d8889-5a9e-4ea8-bddb-239e9979c5e5",  # Email
                                    "value": client.get('Email') or ''
                                },
                                {
                                    "id": "4bd4deaa-fbc8-4086-85ca-f0c803a34a4e",  # LS Email
                                    "value": client.get('LS Email') or ''
                                }
                            ]
                        }
                        
                        req = urllib.request.Request(
                            url,
                            data=json.dumps(data).encode('utf-8'),
                            headers={
                                'Authorization': os.environ.get('CLICKUP_TOKEN'),
                                'Content-Type': 'application/json'
                            }
                        )
                        
                        try:
                            response = urllib.request.urlopen(req)
                            response_data = response.read().decode('utf-8')
                            
                            self.send_response(200)
                            self.end_headers()
                            self.wfile.write(f'SUCCESS: Created task "{task_name}" with custom fields'.encode())
    
                        except urllib.error.HTTPError as e:
                            error_body = e.read().decode('utf-8')
                            self.send_response(500)
                            self.end_headers()
                            self.wfile.write(f'ERROR: {e.code} - {error_body}'.encode())
                            
                    else:
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(b'SKIPPED: No name provided')
                else:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b'SKIPPED: Add to Clickup not checked')
            else:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'IGNORED: Not a row update event')
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f'ERROR: {str(e)}'.encode())