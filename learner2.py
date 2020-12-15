import math
import sys
from File_Loader import *
from PrettyPrint import *
from Logistics import *
from Validation import *

eta = .0000001
iterations = 80000

E = file_loader("appledata.txt")
V = file_loader("applevalid.txt")
w = Logistics(E, eta, iterations)
error = validation(V, w)
pretty_print(w, eta, iterations, error)