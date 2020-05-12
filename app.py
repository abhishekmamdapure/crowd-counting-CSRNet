#importing required libraries 

import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import json

# Custom Imports 
from model import CSRNet
import numpy as np
import PIL.Image as Image
from torchvision import transforms
import matplotlib.pyplot as plt
import random
import io
from PIL import Image
from torchvision import models
import torchvision.transforms as transforms
import torch

def get_model():
    model = CSRNet()
    model = model.cuda()
    checkpoint = torch.load('0model_best.pth.tar')
    model.load_state_dict(checkpoint['state_dict'])
    return model

# Access commons
model = get_model()
# Standard RGB transform
transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),])

def get_prediction(file):
    img = transform(Image.open(file).convert('RGB')).cuda()
    # img = img.cpu()
    output = model(img.unsqueeze(0))
    prediction = int(output.detach().cpu().sum().numpy())
    x = random.randint(1,100000) 
    density = 'static/density_map'+str(x)+'.jpg' 
    plt.imsave(density, output.detach().cpu().numpy()[0][0]) 
    return prediction,density


UPLOAD_FOLDER = './static/'
ALLOWED_EXTENSIONS = set(['.png','.jpg','.jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['POST','GET'])

def upload_file():
    if request.method == 'POST':
        # Remove existing images in directory
        files_in_dir = os.listdir(app.config['UPLOAD_FOLDER'])
        filtered_files = [file for file in files_in_dir if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png")]
        for file in filtered_files:
            path = os.path.join(app.config['UPLOAD_FOLDER'], file)
            os.remove(path)

            # Upload new file
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']

        if not file:
            return
        
        print("GETTING PREDICTION")

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        prediction, density = get_prediction(file)

        return render_template('result.html', Prediction=prediction,Density=density,File=filename) 
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)




