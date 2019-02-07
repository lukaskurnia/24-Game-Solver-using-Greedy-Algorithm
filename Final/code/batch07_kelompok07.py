import backend
import sys

# Activate : py front2proto1.py <input>.txt <output>.txt

if len(sys.argv) == 3:
    sop = sys.argv[1]
    fop = open(sop, 'r')
    line = fop.read()
    fop.close()

    number = line.split()
    number[0] = float(number[0])
    number[1] = float(number[1])
    number[3] = float(number[3])
    number[2] = float(number[2])
    result = backend.algorithm24(number)

    scl = sys.argv[2]
    fcl = open(scl, 'w')
    fcl.write(result)
    fcl.close()
else:
    print('Invalid arguments...')
