import math

def printArray(array):
	for i in range (0, len(array)):
		print str(array[i]) + ' ',

def swapArrayVals(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp

def insertionSort(array):
	sortedArray = [array[0]]
	for i in range (0, len(array)):
		for j in range (0, len(sortedArray)):
			if array[i] <= sortedArray[j]:
				if i == 0:
					sortedArray.pop(0)
				sortedArray.insert(j, array[i])
				break

			if j == len(sortedArray) - 1:
				sortedArray.insert(j + 1, array[i])

	for k in range (0, len(sortedArray)):
		print str(sortedArray[k]) + ' ',

def partition(array, low, high):
	pivot = array[high]
	i = low - 1

	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			swapArrayVals(array, i, j)

	swapArrayVals(array, i + 1, high)
	return i + 1

def partition2dArray(array, low, high, arraySortIndex):
	pivot = array[high][arraySortIndex]
	i = low - 1

	for j in range(low, high):
		if array[j][arraySortIndex] <= pivot:
			i = i + 1
			swapArrayVals(array, i, j)

	swapArrayVals(array, i + 1, high)
	return i + 1

def quickSort(array, low, high):
	if low < high: # Just so no errors?
		pI = partition(array, low, high)

		quickSort(array, low, pI - 1)
		quickSort(array, pI + 1, high)

def quickSort2dArray(array, low, high, arraySortIndex):
	if low < high: # Just so no errors?
		pI = partition2dArray(array, low, high, arraySortIndex)

		quickSort2dArray(array, low, pI - 1, 1)
		quickSort2dArray(array, pI + 1, high, 1)

def asciiSpiralWithLimits(iterations, xLim, yLim):
	# r = theta
	w, h = 2, iterations
	arrayPoints = [[0 for a in range(w)] for b in range(h)]
	for i in range(iterations):
		if int(round(i * math.cos(i * math.pi / 180))) < -1 * xLim or int(round(i * math.cos(i * math.pi / 180))) > xLim or int(round(i * math.sin(i * math.pi / 180))) < -1 * yLim or int(round(i * math.cos(i * math.pi / 180))) > yLim:
			break
		else:
			arrayPoints[i][0] = int(round(i * math.cos(i * math.pi / 180)))
			arrayPoints[i][1] = int(round(i * math.sin(i * math.pi / 180)))
	"""
	quickSort2dArray(arrayPoints, 0, iterations - 1, 0)
	if arrayPoints[0][0] < 0:
		# print arrayPoints[0][0]
		shift = arrayPoints[0][0]
		for j in range(iterations):
			arrayPoints[j][0] = arrayPoints[j][0] + (-1 * shift)
	quickSort2dArray(arrayPoints, 0, iterations -1, 1)
	for k in range(iterations):
		# print arrayPoints[k][0]
		# if k != 0 and arrayPoints[k - 1][1] == arrayPoints[k][1]:
			# print ' ' * (arrayPoints[k][0] - arrayPoints[k - 1][0] - 1) + '.'
			# print arrayPoints[k][0]
		# else:
			# print ' ' * (arrayPoints[k][0] - 1) + '.'
		print ' ' * (arrayPoints[k][0] - 1) + '.'
	"""
	return arrayPoints


def asciiSpiral(iterations):
	# r = theta
	w, h = 2, iterations
	scale = float(1)/(iterations/100 * 2)
	print scale
	arrayPoints = [[0 for a in range(w)] for b in range(h)]
	for i in range(iterations):
		arrayPoints[i][0] = int(round(scale*i * math.cos(i * math.pi / 180)))
		arrayPoints[i][1] = int(round(scale*i * math.sin(i * math.pi / 180)))
	quickSort2dArray(arrayPoints, 0, iterations - 1, 0)
	if arrayPoints[0][0] < 0:
		shift = arrayPoints[0][0]
		for j in range(iterations):
			arrayPoints[j][0] = arrayPoints[j][0] + (-1 * shift)
	quickSort2dArray(arrayPoints, 0, iterations - 1, 1)
	if arrayPoints[0][1] < 0:
		shift = arrayPoints[0][1]
		for j in range(iterations):
			arrayPoints[j][1] = arrayPoints[j][1] + (-1 * shift)

	return arrayPoints













