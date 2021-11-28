import cv2
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as nnf
from pathlib import PurePath
from Model.test_model_pokemon_list import list_of_Pokemon

def net(model_path):
	''' 
    '''
	model = torchvision.models.vgg16(pretrained=True)

	for param in model.parameters():
		param.requires_grad = False

	model.features[0] = nn.Conv2d(3,64,kernel_size=(3,3), stride=(1,1), padding=(1,1))
	model.classifier[6] = nn.Linear(4096,3)

	# model.load_state_dict(torch.load(model_path))

	return model

def image_predictor(net,image, IMG_SIZE):
	'''
    '''
	img = cv2.imread(image)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
	X = torch.Tensor(img).view(-1,3,IMG_SIZE ,IMG_SIZE )
	X = X/255.0

	with torch.no_grad():
		net_out = model(X.view(-1, 3, IMG_SIZE , IMG_SIZE ))[0]
		predicted_class = torch.argmax(net_out)

		sm = torch.nn.Softmax(dim = -1)
		probabilities = sm(net_out) 

		confidence = torch.round(probabilities[predicted_class]*100)
	return X, predicted_class, confidence

def get_prediction(image_path):
    """
    """
    model_path = "Model/test_model.pth"
    IMG_SIZE = 80

    pokemon = list_of_Pokemon
    model = net(model_path)
    X, predicted_class, confidence = image_predictor(net,uploaded_file, IMG_SIZE)
    prediction = f"It's a {pokemon[predicted_class]} with a confidence of {confidence}%"
    
    return prediction
