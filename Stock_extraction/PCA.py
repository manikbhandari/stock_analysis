from csv import reader
from matplotlib.mlab import PCA
import numpy

f =  open('./Google.csv', 'r')
data = list(reader(f))
myData = numpy.array(data)
data = myData[1:,1:]

myData = numpy.array(data).astype(numpy.float)
results = PCA(myData)

print(results.fracs)
print(results.Y)