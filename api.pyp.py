import os, io
from google.cloud import vision
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"ServiceAccountToken.json"

client = vision.ImageAnnotatorClient()

file_name = 'cable car.jpg'
image_path = f'.\VisionAPI\Images\{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# construct an iamge instance
image = vision.types.Image(content=content)

"""
# or we can pass the image url
image = vision.types.Image()
image.source.image_uri = 'https://edu.pngfacts.com/uploads/1/1/3/2/11320972/grade-10-english_orig.png'
"""
#image.source.image_url (we need to upload own api where images are stored & Drive link too)
# annotate Image Response
response = client.text_detection(image=image)  # returns TextAnnotation
df = pd.DataFrame(columns=['locale', 'description'])

texts = response.text_annotations
for text in texts:
    df = df.append(
        dict(
            locale=text.locale,
            description=text.description
        ),
        ignore_index=True
    )

print(df['description'][0])
