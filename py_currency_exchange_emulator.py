class Currency:

  currencies =  {'CHF': 0.930023,
                 'CAD': 1.264553,
                 'GBP': 0.737414,
                 'JPY': 111.019919,
                 'EUR': 0.862361,
                 'USD': 1.0}
      
  def __init__(self, value, unit='USD'):
    self.value = value
    self.unit = unit
  
  def changeTo(self, new_unit):
    self.value = (self.value / Currency.currencies[self.unit] * Currency.currencies[new_unit])
    self.unit = new_unit
    
  def __repr__(self):
      return f"{round(self.value,2)} {self.unit}"

  def __str__(self):
      return f"{round(self.value,2)} {self.unit}"
    
  def __add__(self,other):
      if type(other) == int or type(other) == float:
        n = (other * Currency.currencies[self.unit])
      else:
        n = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
      return Currency(n + self.value, self.unit)

  def __iadd__(self, other):
      return Currency.__add__(self,other)
  
  def __sub__(self,other):
    if type(other) == int or type(other) == float:
      n = (other * Currency.currencies[self.unit])
    else:
      n = (other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit])
    return Currency(n - self.value, self.unit)
  
  def __rsub__(self,other):
    res = other - self.value
    res = Currency(res,self.unit)
    if self.unit !='USD':
      res.changeTo('USD')
    return res
  def __radd__(self,other):
    res = other + self.value
    res = Currency(res,self.unit)
    if self.unit != 'USD':
      res.changeTo('USD')
    return res
  
  def __isub__(self, other):
      return Currency.__sub__(self,other)

v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
print(v1 + v2)
print(v2 + v1)
print(v1 + 3) 
print(3 + v1)
print(v1 - 3) 
print(30 - v2) 