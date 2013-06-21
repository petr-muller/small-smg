'''
Created on Jun 21, 2013

@author: Petr Muller
'''

class SMGPlotter(object):
  def __init__(self):
    self.counter = 0
  
  def getHeader(self):
    return "digraph smg {\n"
  
  def objAsDot(self, obj):
    return '  obj%s [ color=black, shape=rectangle, label="%s" ];\n' % (obj.getId(), str(obj))
  
  def ptAsDot(self, pt):
    return '  val%s -> obj%s[label="+%ib"];\n' % (pt.getValue().getId(), pt.getObject().getId(), pt.getOffset())
  
  def hvAsDot(self, hv):
    if hv.getValue().getId() == 0:
      ret = '  null%i [ label=NULL shape=plaintext ] ;\n' % self.counter
      ret += '  obj%s -> null%i[label="%s@%i"];\n' % (hv.getObject().getId(), self.counter, hv.getDataType(), hv.getOffset())
      self.counter += 1
      return ret
    else:         
      return '  obj%s -> val%s[label="%s@%i"];\n' % (hv.getObject().getId(), hv.getValue().getId(), hv.getDataType(), hv.getOffset())
  
  def valAsDot(self, val):
    return '  val%s;\n' % val.getId()
  
  def getFooter(self):
    return '}\n'

  def plot(self, smg, stream):
    stream.write(self.getHeader())

    for obj in smg.getObjects():
      if obj.getId() != 0:
        stream.write(self.objAsDot(obj))
        for hv in obj.getHVEdges():
          stream.write(self.hvAsDot(hv))
        for pt in obj.getPTEdges():
          stream.write(self.ptAsDot(pt))

    for val in smg.getValues():
      if val.getId() != 0:
        stream.write(self.valAsDot(val))

    stream.write(self.getFooter())  