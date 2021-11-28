
from google.cloud import vision
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"ServiceAccountToken.json"

client = vision.ImageAnnotatorClient()

file_name = 'license cards.jpg'
image_path = f'.\VisionAPI\Images\{file_name}'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# construct an iamge instance
image = vision.types.Image(content=content)

"""
# or we can pass the image url
image = vision.types.Image()
image.source.image_uri = 'https://drive.google.com/drive/folders/1SlVxRwslfJPqLMrab4eSmFvrk7KD2hcA?usp=sharing
' #here we need to put the original url or api
"""

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

#output be like: Registration No. HR42-A-4854
                 Chasis No. MA3EED81S00628175
                 Engine No. F10DN4452456
                 Name : ASHWAN
