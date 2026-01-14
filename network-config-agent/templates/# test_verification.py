# test_verification.py
import requests
import base64

def test_verification():
    # Test API endpoint
    response = requests.post('http://localhost:5000/api/capture-face')
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Test with sample image
    with open('sample_face.jpg', 'rb') as f:
        files = {'face_image': f}
        response = requests.post('http://localhost:5000/api/capture-face', files=files)
        print(f"Verification Result: {response.json()}")

if __name__ == '__main__':
    test_verification()