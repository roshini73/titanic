import csv
import operator

def main():
  info = loadCsvData('titanic.csv')
  prob(info, 'female', '1')
  expec(info, '1')

#calculates expectation of fare conditioned on passenger-class
def expec(matrix, pclass):
  x = 0
  count = 0
  for row in range(len(matrix)):
    if matrix[row][1] == pclass:
      x += float(matrix[row][7])
      count += 1
  print (float (x)/float (count))

#calculates conditional probability a person survives given gender and passenger-class
def prob(matrix, gender, pclass):
  num = 0
  denom = 0
  for row in range(len(matrix)):
    if matrix[row][1] == pclass and matrix[row][3] == gender:
      denom += 1
      if matrix[row][0] == '1':
        num += 1
  print (float (num)/float (denom))

#loads data from provided text file into array
def loadCsvData(fileName):
	matrix = []
	# open a file
	with open(fileName) as f:
		reader = csv.reader(f)

		# loop over each row in the file
		for row in reader:

			# cast each value to a float
			doubleRow = []
			for value in row:
				doubleRow.append(value)

			# store the row into our matrix
			matrix.append(doubleRow)
	return matrix

def printData(matrix):
	for row in matrix:
		print row

# This if statement passes if this
# was the file that was executed
if __name__ == '__main__':
	main()

