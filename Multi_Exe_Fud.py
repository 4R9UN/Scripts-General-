import os, shutil
import subprocess
import time
import binascii
import sys

dir = "temp"
maindir=os.getcwd()
def chk() :
		av_list = ['AVAST Software','AVG','Kaspersky Lab','ESET','Sophos','Microsoft Security Client','Norton Internet Security','Avira','F-Secure']
		os.chdir("C:\Program Files")
		for folders in os.listdir("."):
			if folders in av_list:
				var = folders
				break 
		if var =="AVAST Software":
			pth1 = "C:\Program Files\AVAST Software\Avast"
			print "\n Welcome " + var + " Cli Scan"
		elif var =="AVG":
			pth1 = "C:\Program Files\AVG\AVG2015"	
			print "\n Welcome " + var + " Cli Scan"
		elif var =="F-Secure":
			pth1 = "C:\Program Files\F-Secure\Internet Security\apps\ComputerSecurity\Anti-Virus"	
			print "\n Welcome " + var + " Cli Scan"	
		elif var =="ESET":
			pth1 = "C:\Program Files\ESET\ESET Smart Security"		
			print "\n Welcome " + var + " Cli Scan"
		elif var == "Kaspersky Lab":
			pth1 = "C:\Program Files\Kaspersky Lab\Kaspersky Total Security 16.0.0"
			print "\n Welcome " + var + " Cli Scan"
		elif var == "Sophos":
			pth1 = "C:\Program Files\Sophos\Sophos Anti-Virus"
			print "\n Welcome " + var + " Cli Scan"
		elif var == "Microsoft Security Client":
			pth1 = "C:\Program Files\Microsoft Security Client"	
			print "\n Welcome " + var + " Cli Scan"
		elif var == "Norton Internet Security":
			pth1 = "C:\Program Files\Norton Internet Security\Engine\22.6.0.142"	
			print "\n Welcome " + var + " Cli Scan"
		elif var =="Avira":
			pth1 = "C:\Program Files\Avira\Antivirus"	
			print "\n Welcome " + var + " Cli Scan"	
		else:
			print "AV not available"

def split() :
		os.chdir(maindir)
		path1=maindir + "\\"
		av_list = ['AVAST Software','AVG','Kaspersky Lab','ESET','Sophos','Microsoft Security Client','Norton Internet Security','Avira','F-Secure']
		for files in os.listdir("."):
		
			fileName,fileExtension = os.path.splitext(files)
			if fileExtension.endswith(".exe"):
				b = os.mkdir(fileName)
				block = 5000	
				end = os.path.getsize(files)
				read = open(files,'rb').read()
				strt = 0
				rem = end/block
				for i in range(0,end/block):
					print "block remaining - " + str(rem)
					rem-=1
					for j in range(0,block):
						temp = read[:strt] + "\x00" * block + read[strt+block:]
					fname = fileName + "//" + str(strt) + " - " + str(strt+block) + ".exe"
					write =  open(fname,'wb')
					write.write(temp)
					strt += block 

					os.chdir("C:\Program Files")
					for folders in os.listdir("."):
						if folders in av_list:
							var = folders
							break 
					if var =="AVAST Software":
						pth1 = "C:\Program Files\AVAST Software\Avast"
						pth = "ashCmd.exe \"" + path1 + fileName + "\"" + " /e=100 /p=1	/"	
					elif var =="Avira":
						pth1 = "C:\Program Files\Avira\Antivirus"	
						avf = "C:\\Program Files\\Avira\\Antivirus\\filescan.avp"
						pth = "avscan.exe /CFG=\""+avf+"\" /PATH=\"" + path1 + fileName + ".exe"+"\"" 
					elif var =="AVG":
						pth1 = "C:\Program Files\AVG\AVG2015"			  
						pth = "avgscanx.exe /SCAN=\"" + path1 + fileName +  "\""  + " /CLEAN"
					elif var =="ESET":
						pth1 = "C:\Program Files\ESET\ESET Smart Security"			
						pth = "ecls.exe \"" + path1 +fileName + "\"" + " /adv-heur /action=clean"						
					elif var == "Kaspersky Lab":
						pth1 = "C:\Program Files\Kaspersky Lab\Kaspersky Total Security 16.0.0"
						pth = "avp.com SCAN \"" + path1 + fileName + "\"" + " /i4 /fa"	
					elif var == "Sophos":
						pth1 = "C:\Program Files\Sophos\Sophos Anti-Virus"
						pth = "sav32cli.exe -REMOVE -di -nc -p=\"" + path1 + "\sophos.txt\" " + "\"" + path1 + fileName
					elif var == "Microsoft Security Client":
						pth1 = "C:\Program Files\Microsoft Security Client"
						pth = "MpCmdRun.exe -scan -ScanType 3 -file \"" + path1 + fileName + "\"" 						
					elif var =="F-Secure":
						pth1 = "C:\\Program Files\\F-Secure\\Internet Security\\apps\\ComputerSecurity\\Anti-Virus"
						pth = "fsav.exe fpscan \"" + path1 + fileName + "\"" 
					elif var == "Norton Internet Security":
						pth1 = "C:\\Program Files\\Norton Internet Security\\Engine\\22.6.0.142"	
						pth = "navw32.exe \"" + path1 +  fileName + "\"" + " /automation"
					# elif var =="Avira":
						# pth1 = "C:\Program Files\Avira\Antivirus"	
						# print "\n Welcome " + var + " Cli Scan"							
					else:
						print "AV not available"			
					os.chdir(pth1)
					os.system(pth)
					os.chdir(maindir)
			# ######
			
				for files in os.listdir(fileName + "\\"):
					fileName_1,fileExtension_1 = os.path.splitext(files)
					if fileExtension_1.endswith(".exe"):
						p = os.getcwd() + "\\" + fileName + "\\" + fileName_1 
						b1 = os.mkdir(p)		
						a = files.split(' - ')
					
						strt_1 = int(a[0])
						end_1 = int(a[1][:a[1].find('.')])
						
						block_1 = 100
						rem_1 = end_1/block_1
						read = open(os.getcwd()+"\\"+fileName+".exe",'rb').read()

						for i in range(0,end_1/block_1):
							print "block remaining - " + str(rem_1)
							rem_1-=1
							for j in range(0,block_1):
								temp_1 = read[:strt_1] + "\x00" * block_1 + read[strt_1+block_1:]
							fname_1 = p + "//" + str(strt_1) + " - " + str(strt_1+block_1) + ".exe"
							
							write_1 =  open(fname_1,'wb')
							
							write_1.write(temp_1)
							strt_1 += block_1
					
							os.chdir("C:\Program Files")
							for folders in os.listdir("."):
								if folders in av_list:
									var = folders
									break 
							if var =="AVAST Software":
								pth1 = "C:\Program Files\AVAST Software\Avast"
								pth = "ashCmd.exe \"" + path1 + fileName + "\\"+fileName_1 + "\"" + " /e=100 /p=1	/"	
							elif var =="AVG":
								pth1 = "C:\Program Files\AVG\AVG2015"	
								pth = "avgscanx.exe /SCAN=\"" + path1 + fileName + "\\"+fileName_1 + "\""  + " /CLEAN"
								print pth
							elif var =="ESET":
								pth1 = "C:\Program Files\ESET\ESET Smart Security"			
								pth = "ecls.exe \"" + path1 +fileName + "\\"+fileName_1 + "\"" + " /adv-heur /action=clean"						
							elif var == "Kaspersky Lab":
								pth1 = "C:\Program Files\Kaspersky Lab\Kaspersky Total Security 16.0.0"
								pth = "avp.com SCAN \"" + path1 + fileName + "\\"+fileName_1 + "\"" + " /i4 /fa"	
							elif var == "Sophos":
								pth1 = "C:\Program Files\Sophos\Sophos Anti-Virus"
								pth = "sav32cli.exe -REMOVE -di -nc -p=\"" + path1 + "\sophos.txt\" " + "\"" + path1 + fileName+"\\"+fileName_1  
							elif var == "Microsoft Security Client":
								pth1 = "C:\Program Files\Microsoft Security Client"
								pth = "MpCmdRun.exe -scan -ScanType 3 -file \"" + path1 + fileName +"\\"+fileName_1 +  "\"" 						
							elif var =="F-Secure":
								pth1 = "C:\\Program Files\\F-Secure\\Internet Security\\apps\\ComputerSecurity\\Anti-Virus"
								pth = "fsav.exe fpscan \"" + path1 + fileName +"\\"+fileName_1 +  "\"" 
							elif var == "Norton Internet Security":
								pth1 = "C:\\Program Files\\Norton Internet Security\\Engine\\22.6.0.142"	
								pth = "navw32.exe \"" + path1 +  fileName + "\\"+fileName_1 + "\"" + " /automation"
							else:
								print "AV not available"

							os.chdir(pth1)
							os.system(pth)
							os.chdir(maindir)
def main():
	chk()
	split()
	# scan()
main()
		########
#label .myLabel

# for files in os.listdir("."):
	# fileName,fileExtension = os.path.splitext(files)
	# if fileExtension.endswith(".exe"):
		# b = os.mkdir(fileName)
		
		# block = 1000	
		# end = os.path.getsize(files)
		# read = open(files,'rb').read()
		# strt = 0
		# rem = end/block
				
		# for i in range(0,end/block):
			# print "block remaining - " + str(rem)
			# rem-=1
			# for j in range(0,block):
				# temp = read[:strt] + "\x00" * block + read[strt+block:]
			# fname = fileName + "//" + str(strt) + " - " + str(strt+block) + ".exe"
			# write =  open(fname,'wb')
	
			# write.write(temp)
			# strt += block 
					
			# ######
			
		# for files in os.listdir(fileName + "\\"):
			# fileName_1,fileExtension_1 = os.path.splitext(files)
			# if fileExtension_1.endswith(".exe"):
				# p = os.getcwd() + "\\" + fileName + "\\" + fileName_1 
				# b1 = os.mkdir(p)		
				# a = files.split(' - ')
			
				# strt_1 = int(a[0])
				# end_1 = int(a[1][:a[1].find('.')])
				
				# block_1 = 100
				# rem_1 = end_1/block_1
				# read = open(os.getcwd()+"\\"+fileName+".exe",'rb').read()

				# for i in range(0,end_1/block_1):
					# print "block remaining - " + str(rem_1)
					# rem_1-=1
					# for j in range(0,block_1):
						# temp_1 = read[:strt_1] + "\x00" * block_1 + read[strt_1+block_1:]
					# fname_1 = p + "//" + str(strt_1) + " - " + str(strt_1+block_1) + ".exe"
					
					# write_1 =  open(fname_1,'wb')
					
					# write_1.write(temp_1)
					# strt_1 += block_1
