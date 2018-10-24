# -*- coding: utf-8 -*-



import shapefile 



sf = shapefile.Reader("G:/test/COUNTY_MOI_1070516.shp")
w =  shapefile.Writer()
w.autoBalance = 1

records = sf.records()
fields = sf.fields


field_names = [field[0] for field in fields] 
# construction of a dctionary field_name:value  
i=0
for r in  sf.records():
    if '連江' in r[2]:
         r[3]='test'
         records[i]=r
         #w.record(*r)           
    i=i+1
    

for name in fields:
    if type(name) == "tuple":
        continue
    else:
        args = name
        w.field(*args)

geom = sf.shapes()

for feature in geom:
    # if there is only one part
    if len(feature.parts) == 1:
        # create empty list to store all the coordinates
        poly_list = []
        # get each coord that makes up the polygon
    for coords in feature.points:
           x, y = coords[0], coords[1]
           # tranform the coord
           new_x, new_y = transform(input_projection, output_projection, x, y)
           # put the coord into a list structure
           poly_coord = [float(new_x), float(new_y)]
           # append the coords to the polygon list
           poly_list.append(poly_coord)
       # add the geometry to the shapefile.
       w.poly(parts=[poly_list])
    else:
        # append the total amount of points to the end of the parts list
        feature.parts.append(len(feature.points))
        # enpty list to store all the parts that make up the complete feature
        poly_list = []
        # keep track of the part being added
        parts_counter = 0

        # while the parts_counter is less than the amount of parts
        while parts_counter < len(feature.parts) - 1:
            # keep track of the amount of points added to the feature
            coord_count = feature.parts[parts_counter]
            # number of points in each part
            no_of_points = abs(feature.parts[parts_counter] - feature.parts[parts_counter + 1])
            # create list to hold individual parts - these get added to poly_list[]
            part_list = []
            # cut off point for each part
            end_point = coord_count + no_of_points

            # loop through each part
            while coord_count < end_point:
                for coords in feature.points[coord_count:end_point]:
                    x, y = coords[0], coords[1]
                    # tranform the coord
                    new_x, new_y = transform(input_projection, output_projection, x, y)
                    # put the coord into a list structure
                    poly_coord = [float(new_x), float(new_y)]
                    # append the coords to the part list
                    part_list.append(poly_coord)
                    coord_count = coord_count + 1
        # append the part to the poly_list
        poly_list.append(part_list)
        parts_counter = parts_counter + 1
    # add the geometry to to new file
    w.poly(parts=poly_list)



w.save('G:/test/test.dbf')

ws = shapefile.Reader("G:/test/COUNTY_MOI_1070516.dbf")
records_test = ws.records()
fields_test = ws.fields
