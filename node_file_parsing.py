import re
from Gate import Gate
from ConcatenatedGateList import ConcatenatedGateList

class filePrsing():
    def __init__(self, fileName) -> object:
        """
        :rtype: object
        """
        self._fileName=fileName
        pass

    def getGates(self):
        gates = {'and', 'or', 'not', 'xor','nand','nor'}
        listOfGates = []
        inputs = []
        outPuts = []
        outputPair = []
        #Create an empty gate list
        _list=ConcatenatedGateList()
        i=0
        input1=input2=None
        #Initiate the list of gates from the file
        with open(self._fileName, "r") as file:
            for line in file:
                line = line.lower()
                if 'wire' in line:
                    _list.addWire(line)
                elif 'endmodule' not in line and 'module' in line:
                    outputInd=line.find('output')
                    if (outputInd!=-1):
                        endInd=line.find(',')
                        if (endInd==-1):
                            endInd = line.find(')')
                        outputName=line[outputInd+6:endInd].strip()
                        _list.setOutputName(outputName)
                    ind1 = line.find('input') + 5  # first input ind
                    if (ind1<5):
                        continue    #No entries to the circle
                    ind2 = line[ind1:].find(',') + ind1  # end of first entry definition ind
                    if (ind2<ind1):
                        ind2 = line[ind1:].find(')') + ind1
                    input1 = line[ind1:ind2].strip()    #get the first entry name
                    _list.setFirstInputName(input1)
                    ind3 = line[ind2:].find("input") + 5 + ind2  # second input
                    if (ind3-5>ind2):   #Second input exist
                        ind4 = line[ind3:].find(')') + ind3
                        input2 = line[ind3:ind4].strip()
                    #ins=[input1,input2]
                    _list.setSecInputName(input2)
                    #Add the first circle input to the list
                    listOfGates.append('INPUT')
                    # inputPair = ["CircleInput"]
                    inputPair = [" "]

                    inputPair.append(i)
                    inputs.append(inputPair)
                    outputPair = [input1, i]
                    outPuts.append(outputPair)
                    _list.addGate(Gate("INPUT", inputs[i][0],"",outPuts[i][0], 0,None, input1))
                    i += 1
                    if input2 is None:
                        continue
                    # Add the second circle input to the list
                    listOfGates.append('INPUT')
                    # inputPair = ["CircleInput"]
                    inputPair = [" "]
                    inputPair.append(i)
                    inputs.append(inputPair)
                    outputPair = [input2, i]
                    outPuts.append(outputPair)
                    _list.addGate(Gate("INPUT", inputs[i][0], "", outPuts[i][0], 0,None, input2))
                    i += 1
                elif 'time' in line:
                    _list.addTimeScale(line)
                elif ' and' in line:
                    listOfGates.append('AND')
                    inputPair=line[line.find(',')+1:line.find(')')].split(',')
                    inputPair.append(i)
                    inputs.append(inputPair)
                    outputPair=[line[line.find('(')+1:line.find(',')],i]
                    outPuts.append(outputPair)
                    _list.addGate(Gate("AND", inputs[i][0],inputs[i][1],outPuts[i][0],0))
                    i += 1
                elif ' or' in line:
                    listOfGates.append('OR')
                    inputPair = line[line.find(',') + 1:line.find(')')].split(',')
                    inputs.append(inputPair)
                    inputPair.append(i)
                    outputPair=[line[line.find('(') + 1:line.find(',')],i]
                    outPuts.append(outputPair)
                    _list.addGate(Gate("OR", inputs[i][0], inputs[i][1], outPuts[i][0], 0))
                    i += 1
                elif ' xor' in line:
                    listOfGates.append('XOR')
                    inputPair = line[line.find(',') + 1:line.find(')')].split(',')
                    inputs.append(inputPair)
                    inputPair.append(i)
                    outputPair = [line[line.find('(') + 1:line.find(',')], i]
                    outPuts.append(outputPair)
                    _list.addGate(Gate("XOR", inputs[i][0], inputs[i][1], outPuts[i][0], 0))
                    i += 1
                elif ' nand' in line:
                    listOfGates.append('NAND')
                    inputPair = line[line.find(',') + 1:line.find(')')].split(',')
                    inputs.append(inputPair)
                    inputPair.append(i)
                    outputPair = [line[line.find('(') + 1:line.find(',')], i]
                    outPuts.append(outputPair)
                    _list.addGate(Gate("NAND", inputs[i][0], inputs[i][1], outPuts[i][0], 0))
                    i += 1
                elif ' nor' in line:
                    listOfGates.append('NOR')
                    inputPair = line[line.find(',') + 1:line.find(')')].split(',')
                    inputs.append(inputPair)
                    inputPair.append(i)
                    outputPair=[line[line.find('(') + 1:line.find(',')],i]
                    outPuts.append(outputPair)
                    _list.addGate(Gate("NOR", inputs[i][0], inputs[i][1], outPuts[i][0], 0))
                    i += 1
                elif ' not' in line:
                    listOfGates.append('NOT')
                    ind1 = line.find(',') + 1
                    ind2 = line.find(')')
                    subLine = line[ind1:ind2]
                    inputPair = subLine.split(',')
                    inputPair.append(i)
                    inputs.append(inputPair)
                    outputPair=[line[line.find('(') + 1:line.find(',')],i]
                    outPuts.append(outputPair)
                    _list.addGate(Gate("NOT", inputs[i][0],"", outPuts[i][0], 0))
                    i += 1
                else:
                    gateTpe = ''
                    continue

        return _list




