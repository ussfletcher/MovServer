import sys
import os
import scanTorrents
import generateBackdrops
import commonSettings
import databaseSetup

#Print the correct usage syntax
def printUsage():
	print 'Usage: movServer [-argument]'

#Print the valid arguments that may be passed
def printValidArguments():
	print 'Valid arguments are:\n\t s: Scan torrent folder\n\t g: Gather server information\n\t b: Create picture backdrops'

#Grab all the user passed arguments and check them for validity
#Return: the argument
def grabArguments():
	if len(sys.argv) < 2:
		argument = None
	elif len(sys.argv) > 2:
		printUsage()
	elif len(sys.argv[1]) > 1:
		if sys.argv[1][0] != '-':
			printUsage()
		else:
			argument = sys.argv[1][1:]
			if argument != 's' and argument != 'g' and argument != 'b':
				printValidArguments()
	else:
		printUsage()
	return argument

#Check if this is the first run of movServer
def isFirstRun():
	home = os.getenv('HOME')
	configDir = '.movServer'
	if os.path.exists(os.path.join(home, configDir)):
		return False
	else:
		return True

#Main program execution 
def main():
	argument = grabArguments()
	if argument == 's':
		scanTorrents.main()
	elif argument == 'g':
		systemConf = commonSettings.systemSettings()
		databaseSetup.resetTables(systemConf)
		databaseSetup.createTables(systemConf)
	elif argument == 'b':
		generateBackdrops.main()
	elif argument == None:
		scanTorrents.main()
	else:
		print 'There was an issue starting movServer'
		
main()
