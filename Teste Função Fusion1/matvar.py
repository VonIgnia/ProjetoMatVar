### MatVar.py (esse arquivo) foi utilizado apenas como material de referencia para a compreensão de como funciona ### 
### o uso de add-ins para a plotagem de gráficos no aplicativo da Autodesk Fusion 360 e foi copiado de ##############
### https://gist.github.com/Capo01/5595313ddf0e3c9bf892e79fac1a00b4 Fusion 360 equation driven curve API example ####
### No entanto ele não foi utilizado para nada além de estudos e não deve ser considerado para correção. ############

import adsk.core, adsk.fusion, adsk.cam, traceback, math

def run(context):
	ui = None
	try:
		app = adsk.core.Application.get()
		ui = app.userInterface
		design = app.activeProduct
		# Get the root component of the active design.
		rootComp = design.rootComponent
		# Create a new sketch on the xy plane.
		sketches = rootComp.sketches
		xyPlane = rootComp.xYConstructionPlane
		sketch = sketches.add(xyPlane)
		points = adsk.core.ObjectCollection.create() # Create an object collection for the points.
		
		# Enter variables here. E.g. E = 50
		startRange = 0 # Start of range to be evaluated.
		endRange = 2*math.pi # End of range to be evaluated.
		splinePoints = 100 # Number of points that splines are generated.
		# WARMING: Using more than a few hundred points may cause your system to hang.
		i = 0

		while i <= splinePoints:
			t = startRange + ((endRange - startRange)/splinePoints)*i
			xCoord = (math.sin(2*t))
			yCoord = (math.sin(3*t))

			points.add(adsk.core.Point3D.create(xCoord,yCoord))
			i = i + 1
			
		#Generates the spline curve
		sketch.sketchCurves.sketchFittedSplines.add(points)
	
	# Error handeling
	except:
		if ui:
			ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))