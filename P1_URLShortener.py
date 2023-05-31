import hashlib
import base64

class URLShortener:
    def __init__(self):
        self.url_dict = {}

    def shorten_url(self, original_url):
        # Generate MD5 hash of the original URL
        hash_object = hashlib.md5(original_url.encode())
        hash_value = hash_object.digest()

        # Base64 encode the hash value
        base64_encoded = base64.urlsafe_b64encode(hash_value)
        short_url = base64_encoded[:6].decode()

        # Store the original URL and corresponding short URL
        self.url_dict[short_url] = original_url

        return short_url

    def get_original_url(self, short_url):
        if short_url in self.url_dict:
            return self.url_dict[short_url]
        else:
            return None

# Usage example
shortener = URLShortener()
original_url = "https://example.com/very-long-url-with-lots-of-characters"
short_url = shortener.shorten_url(original_url)
print(f"Short URL: {short_url}")

retrieved_url = shortener.get_original_url(short_url)
print(f"Retrieved URL: {retrieved_url}")
