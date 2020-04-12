#Imports PyTorch Library
import torch

#Imports NumPy Library
import numpy as nump

#Imports the matlabplot.pyplot Function
import matlabplot.pyplot as pyp

#Creates a vector with end values being between -1 and 1 with a size of 10
a = nump.linspace(-1, 1, 10)

#Applies tangent function and sotres result in the variable b
b = torch.tan(torch.FloatTensor(a))

print(b)

#Visually plot the outputted result
pyp.plot(a, b.numpy(), color = 'blue', marker = "o")
pyp.title("torch.tan Example")
pyp.xlabel ("X")
pyp.ylabel ("Y")

pyp.show()