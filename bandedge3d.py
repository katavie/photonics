from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

'''
this script parses x and z correctly 

TODO:
	parse y values correctly
	pass file in as param
'''

x = [] # distance along x-axis (nm)
y = [] # distance along y-axis (nm)
z = [] # band energy (eV)

with open('bandedge3d.fld') as f:
	lines = list(f)

	lineIndex = 0
	newLineNum = 0
	dataIndex1 = 1 # refers to sections of bulk data in .fld
	dataIndex2 = 1

	while lineIndex < len(lines): # parse through all lines and populate lists

		if str(lines[lineIndex])[:2] == ' \n' or str(lines[lineIndex])[:1] == '\n': # if line is space-newline or simply newline

			newLineNum += 1
			print(newLineNum)

			# check subsquent lines
			while str(lines[lineIndex + dataIndex1])[4:5] == '.': # if 4th char is decimal point

				if newLineNum == 3: # 3rd space-newline/newline ends header, starts x-coordinate data
					x.append(str(lines[lineIndex + dataIndex1][3:-1])) # remove spaces and \n

				if newLineNum == 4:
					y.append(str(lines[lineIndex + dataIndex1][3:-1]))
				dataIndex1 += 1

			if newLineNum == 6: # skip over 5, which starts z-coordinates
				while str(lines[lineIndex + dataIndex2])[5:6] == '.' and lineIndex + dataIndex2 < len(lines) - 1:
					z.append(str(lines[lineIndex + dataIndex2])[4:17])
					dataIndex2 += 1

		lineIndex += 1