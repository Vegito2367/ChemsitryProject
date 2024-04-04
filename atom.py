class Atom:
  def __init__(self, inputList):
    elemname=inputList.pop(0)
    self.identifier=elemname
    ind1,ind2=0,0
    for i in range(len(elemname)):
      if(str.isdecimal(elemname[i])):
        ind1=i
        break
    for i in range(len(elemname)-1,-1,-1):
      if(str.isdecimal(elemname[i])):
        ind2=i
        break
    
    if(ind1==0 and ind2==0):
      self.atomLetter=""
      self.atomNum=1
      self.element=elemname
    else:
      self.atomLetter=elemname[ind2+1:]
      self.element=elemname[:ind1]
      self.atomNum=elemname[ind1:ind2+1]



    self.symbol=inputList.pop(0)
    self.positionVector=[inputList.pop(0),inputList.pop(0),inputList.pop(0)]
    for v in range(3):
      elem=self.positionVector[v]
      if ('(' in elem ):
        self.positionVector[v]=float(elem[:elem.index("(")])
      else:
        self.positionVector[v]=float(elem)
    self.remainingNumbers=inputList
  
  def __str__(self):
    atomletter="No letter" if self.atomLetter=="" else self.atomLetter
    return f"Name: {self.element}, symbol: {self.symbol} position : {self.positionVector}, elemNum: {self.atomNum}, atom letter: {atomletter}\n"
  
  def __repr__(self):
    return self.identifier
  

  def getDistance(self,other):
    distanceVector=[round(self.positionVector[i]-other.positionVector[i],6) for i in range(3)]
    output=0
    for j in distanceVector:
      output+=j**2
    
    return round(output**0.5,6)

  