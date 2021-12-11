# how to test wheter python reloads a module if you import it after modification

import time
import importlib as il

while True:
	time.sleep(0.5)
	import module
	il.reload(module)
	module.funct()
