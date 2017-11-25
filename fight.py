
import cognitive_face as CF
import json

def main(image1, image2):
    """
    takes two image locations
    Returns a winner out of the two images
    :param image1:
    :param image2:
    :return: 1 or 2
    """
    KEY = '8b9d5cf6d62e4b5d9436f59acd5e0ba4'  # Replace with a valid subscription key (keeping the quotes in place).
    CF.Key.set(KEY)

    img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'

    BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)

    result = CF.face.detect(img_url)
    print(result)

    print("Getting face data")
    face1 = CF.face.detect(image1)
    face2 = CF.face.detect(image2)
    print("tried to get faces")
    json1 = json.loads(face1)
    print(face1)
    print(face2)

    print(image1, image2)
    return(1)