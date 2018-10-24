#! /usr/bin/env python
#-*- coding:utf-8 -*-


from qgis import *
import qgis.utils
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# import vector layer
layer = iface.addVectorLayer("D:/data/48_d.shp", "test", "ogr")
if not layer:
	print "Layer failed to load!"
	
	
#for field in layer.pendingFields():
#	print field.name(), field.typeName()
	


a1= u"住宅"
a1=a1.decode('utf8').encode('ascii')
a2=u"住"
a2=a2.decode('utf8').encode('ascii')
iter = layer.getFeatures()
for feature in iter:
	# retrieve every feature with its geometry and attributes
	# fetch geometry
	geom = feature.geometry()
	#print "Feature ID %d: " % feature.id()
	# show some information about the feature
	#if geom.type() == QGis.Point:
	#	x = geom.asPoint()
	#	print "Point: " + str(x)
	#elif geom.type() == QGis.Line:
	#	x = geom.asPolyline()
	#	print "Line: %d points" % len(x)
	#elif geom.type() == QGis.Polygon:
	#	x = geom.asPolygon()
	#	numPts = 0
	#	for ring in x:
	#		numPts += len(ring)
	#	print "Polygon: %d rings with %d points" % (len(x), numPts)
	#	
	#else:
	#	print "Unknown"
	# 表單紀錄
	attrs = feature.attributes()
	# 表單
	print attrs[3]
	if a1 in attrs[3]:
		attrs[17]=u"住"
		print "test"
