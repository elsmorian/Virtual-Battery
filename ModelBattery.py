class ModelBattery:
  
  Name = "ModelBattery"
  Version = "V 0.2"
  
  def __init__(self, voltage, ampHours):
    self.voltage = voltage
    self.wattHourCapacity = voltage * ampHours
    self.currentCapacity = self.wattHourCapacity
  
  def __str__(self):
    rtnStr = "A "+str(self.voltage)+"V battery with "+str(self.getPercentCurrentCharge())+"% of "
    rtnStr += str(self.wattHourCapacity)+"Wh capacity remaining."
    return rtnStr
  
  def sensorUpdate(self, update):
    self.currentCapacity += update
    if self.currentCapacity > self.wattHourCapacity:
      self.currentCapacity = self.wattHourCapacity
  
  def drain(self, ampHour):
  	#print "BATT DRAIN: draining with: "+str(ampHour)
    self.currentCapacity -= ampHour
  
  def charge(self, ampHour):
    self.currentCapacity += ampHour
    if self.currentCapacity > self.wattHourCapacity:
      self.currentCapacity = self.wattHourCapacity
  
  def getCurrentCharge(self):
    return self.currentCapacity
  
  def getPercentCurrentCharge(self):
    percent = (self.currentCapacity / float(self.wattHourCapacity) )*100
    return round(percent,2)
    
  def getVoltage(self):
    return self.voltage
  
  def getCapacity(self):
    return self.wattHourCapacity
  
  def setFullyCharged(self):
    self.currentCapacity = self.wattHourCapacity
  
  def setEmpty(self):
    self.currentCapacity = 0


class ModelPanel:
  
  Name = "ModelPanel"
  Version = "V 0.1"
  
  def __init__(self, voltage, powerRating):
    self.voltage = voltage
    self.powerRating = powerRating
    self.generatingPower = 0
  
  def setCurrentGenerationCurrent(self, amps):
    self.generatingPower = self.voltage * amps
    