import qrcode,requests,os
from urllib.parse import urlparse
print("-"*3+" QRCODE GENERATOR BY URL "+"-"*3)
url_input = input("Enter URL: ").strip()
if not url_input.startswith(("http://", "https://")):url_input = "https://" + url_input
parsed = urlparse(url_input)
is_valid_structure = bool(parsed.scheme and parsed.netloc)
if not is_valid_structure:print("❌ Error: The URL format is invalid.")
else:
    try:
        print("Checking if website is online...")
        response = requests.head(url_input, timeout=3, allow_redirects=True)
        if response.status_code < 400:
            qr_image = qrcode.make(url_input)
            print("Website online!")
            file_name = str(input("What would you like to name this QR Code: "))+".png"
            qr_image.save(file_name)
            print(f"✅ Success! Your QR code has been saved as '{file_name}' at {os.path.dirname(os.path.abspath(__file__))}")
        else:print(f"❌ Error: Website returned an error code ({response.status_code}).")
    except requests.exceptions.RequestException: print("❌ Error: Could not connect to the website. It might be down or typed incorrectly.")