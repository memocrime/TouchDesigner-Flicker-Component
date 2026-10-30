from TDStoreTools import StorageManager
import TDFunctions as TDF

class componentCreationEXT:
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
	
	def find_external_ops(self):
		tox = op.COMPCREATE.findChildren(type=COMP) # Find all comps in network and create a list from it
		external = [t for t in tox if t.par.externaltox != ''] # Find all comps with a path in external tox
		return external
	def SaveExternalizedTox(self):
		# Get the external ops and save them in the same location as the external counterpart
		# This is triggered on project pre-save
		ext = self.find_external_ops()
		
		for op in ext:
			op.save(op.par.externaltox.eval())
