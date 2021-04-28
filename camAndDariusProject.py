import re
import cmath


# Calculates the quadratic
def quadraticCalculator(a, b, c):
	# calculating  the discriminant
	dis = (b**2) - (4 * a*c)
	
	# find two results
	ans1 = (-b-cmath.sqrt(dis))/(2 * a)
	ans2 = (-b + cmath.sqrt(dis))/(2 * a)
	
	# printing the results
	print('The roots are')
	print(ans1)
	print(ans2)


# Checks to see if it a character within the term
regexTerm = r"([+-]?[^-+]+)"

# Checks to see if it is a variable
regexVar = r"([a-zA-Z])"

# Checks to see if the power of the term equals 2
regexFact2 = r"(\^2)$"

# Checks to see if there are any powers greater than 2 or less than 0
regexInvalid = r"(\^[3-9]|\^[+-])"

# Checks to see if there are any digits following a carat
regexInvalid2 = r"([a-z][0-9]+)"

# Checks the integer values of each term
regexInt = r"(^[0-9+-]*)"

# Gets input and separates them into different lists
poly = input("Enter a quadratic polynomial: ")


# Checks to see if the input is invalid and adds them to a list
invalidList = re.findall(regexInvalid, poly)
invalidList += re.findall(regexInvalid2, poly)

# Outputs the equation variable to a set, if the set has more than one item, the equation is invalid
equationVar = set(re.findall(regexVar, poly))
equationVarList = list(equationVar)
equationVarLength = len(equationVar)

#Sets the output to a spaceless polynomial equation
output = re.findall(regexTerm, poly.replace(" ", ""))

#Lists of terms
fact2 = []
fact2Ints = []
fact2Total = 0

fact1 = []
fact1Ints = []
fact1Total = 0

constants = []
constantsTotal = 0

# Checks to see if it is a quadratic equation and then separates the terms into their distinct categories
if equationVarLength > 1 or len(invalidList) != 0:
	print("This is not a quadratic equation!")
	print("Invalid parse: ", invalidList)

else:
	for squaredTerm in output:

		# Checks to see if there are any square terms
		if len(re.findall(regexFact2, squaredTerm)) != 0:

			# Captures the square terms and appends them to a list
			fact2.append(squaredTerm)

			# Checks to see if the leading coefficient is an assumed 1, else appends the integer to a list
			if (re.findall(regexInt, squaredTerm)[0] == '+') or (re.findall(regexInt, squaredTerm)[0] == '-') or (re.findall(regexInt, squaredTerm)[0] == ''):
				fact2Ints.append(re.findall(regexInt, squaredTerm)[0] + '1')
			else:
				fact2Ints.append(re.findall(regexInt, squaredTerm)[0])

			# Adds the coefficient to a running total of like terms
			fact2Total += int(fact2Ints[-1])

	for fact1Term in output:

		# Checks to see if there are any power 1 variable terms
		if fact1Term[-1] == equationVarList[0]:
			
			# Captures the power 1 variable terms and appends them to a list
			fact1.append(fact1Term)

			# Checks to see if the leading coefficient is an assumed 1, else appends the integer to a list
			if (re.findall(regexInt, fact1Term)[0] == '+') or (re.findall(regexInt, fact1Term)[0] == '-') or (re.findall(regexInt, fact1Term)[0] == ''):
				fact1Ints.append(re.findall(regexInt, fact1Term)[0] + '1')
			else:
				fact1Ints.append(re.findall(regexInt, fact1Term)[0])

			# Adds the coefficient to a running total of like terms
			fact1Total += int(fact1Ints[-1])

	for constTerm in output:
		# Combines the factor 2 and factor 1 terms into one list
		facts = fact1 + fact2
		
		# Checks to see if the term is in either list, if not appends to constants list and combines like terms
		if constTerm not in facts:
			constants.append(constTerm)
			constantsTotal += int(constants[-1])
	

	#Converts ints to strings if they are greater than or equal to 0
	if (constantsTotal >= 0):
		constantsTotal = "+" + str(constantsTotal)

	if (fact1Total >= 0):
		fact1Total = "+" + str(fact1Total)

	print("Terms are : ", output)

	print(f'Final polynomial is: {fact2Total}{equationVarList[0]}^2 {fact1Total}{equationVarList[0]} {constantsTotal}')
	
	quadraticCalculator(fact2Total, int(fact1Total), int(constantsTotal))