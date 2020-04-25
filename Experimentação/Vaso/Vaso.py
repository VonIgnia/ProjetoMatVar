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
		yzPlane = rootComp.yZConstructionPlane
		sketch = sketches.add(yzPlane) 
		
		# originalmente era o plano xy, no entanto isso foi modificado após algumas rodagens
		# mas isso permitiu a seguinte descoberta, no Fusion é possivel plotar pontos e curvas
		# em um eixo não declarado inicialmente pelo plano, e isso permite a criação de um skecth 3D

	###### Linha vertical do ponto inicial do intervalo (0,0,0 até f(0)) ou "inicio da integral"
		
		#Aviso mudar o valor em z caso seja alterada a função 1
		lines = sketch.sketchCurves.sketchLines
		line1 = lines.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(1, 0,0))

	###### Gráfico 1 ### f(x) = Se(0 ≤ x ≤ 4.2, -0.02 (4x³ - 18x²) + 1) ######

		points = adsk.core.ObjectCollection.create() # essa linha deve ser chamada no início de todos os gráficos, pois reseta a "lista" de pontos

		startRange = 0 # Ínicio do intervalo.
		endRange = 4.2 # Fim do intervalo
		splinePoints = 10 # Número de pontos entre o intervalo
		# Aviso: não atribuir á variavel splinePoints valores maiores que algumas centenas, isso evitará crashes do sistema (seu PC agradece)
		
		i = 0
		while i <= splinePoints:
			t = startRange + ((endRange - startRange)/splinePoints)*i
			xCoord = (-0.02*(4*t**3 - 18*t**2) + 1)
			yCoord = t
			zCoord = 0
			#
			points.add(adsk.core.Point3D.create(xCoord,yCoord,zCoord))
			i = i + 1			
		#Generates the spline curve
		sketch.sketchCurves.sketchFittedSplines.add(points)
		
		line2 = lines.addByTwoPoints(adsk.core.Point3D.create(0, t, 0), adsk.core.Point3D.create((-0.02*(4*t**3 - 18*t**2) + 1), t,0))
		line3 = lines.addByTwoPoints(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(0,t,0))
	# Error handeling
	except:
		if ui:
			ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))