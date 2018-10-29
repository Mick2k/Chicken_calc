#!/bin/python3.6
# Import modules for CGI handling
import cgi, cgitb
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields


print ("Conntent-type: text/html\n\n")

#time_per_kg is 40mins
time_per_kg = (int(40))
kg_of_chicken = form.getvalue('weight')
#comment out the above line and uncomment the below to get it to work via CLI

#kg_of_chicken = float(input('Kg of chicken: '))
answer = int(time_per_kg) * float(kg_of_chicken)
#answer 10 & 20 allows for extra time between 10-20mins for cooking
answer10 = (int(answer)+10)
answer20 = (int(answer)+20)


#print ("Conntent-type: text/html\r\n\r\n")
print ('Roast in the centre of a pre-heated oven, gas mark 5,190C, for 40 minutes per kg, plus 10-20 minutes extra, the ranges are below')
print ('Cooking time is %s to %s minutes' % (answer10, answer20))

