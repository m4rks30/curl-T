import os
import sys
import httplib2

filename = input("Enter file path: ")
url = input("Enter server URL: ")

try:
    http_obj = httplib2.Http()

    with open(filename, 'rb') as file:
        filename = os.path.basename(filename)
        response, content = http_obj.request(
            url,
            method='POST',
            body=file.read(),
            headers={
                'Content-Disposition': f'attachment; filename="{filename}"',
                'Content-Type': 'application/octet-stream'
            }
        )
    print(response)
    print(content)

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
