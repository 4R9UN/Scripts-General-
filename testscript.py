import os 
import time
import subprocess


vm_path ="D:\machines"
fl = open("result.txt","w")
fl.close()
def proc2list(proc_lst):
    proc_lst = proc_lst.split("\r\n")[1:]
    lst = []
    for pl in proc_lst:
	row = pl.split(",")
	if len(row) > 1:
	    lst.append(row[0].replace("pid=","") + "-" + row[2].replace("cmd=","").replace("[","").replace("]","").strip())        
    return lst
    
path = vm_path 


def vm_chk( b ):
    dict = {'51':'WinXP',
            '60':'WinVista',
            '61':'Win7',
            '62':'Win8',
            '63':'Win8.1',
            '10':'Win10',
            '86':' 32 bit',
            '64':' 64 bit',
            '00':'sp0',
            '01':'sp1',
            '02':'sp2',
            '03':'sp3',
            '07':' Office 2007',
            '13':' Office 2013',}
    
    n = 2
    a = [line[i:i+n] for i in range(0, len(line), n)]
    for i in range (0,len(a)):
	if i==3 and a[i]==10:
	    a[i] = ' Office 2010'
	else:
	    a[i] = dict[a[i]]
    return a[0]+a[2]+a[1]+a[3]+a[5]+a[4]

dict_first = {"86-86":"C:\\Program Files\\",
                 "64-86":"C:\\Program Files (x86)\\"}

dict_middle = {"07":"Microsoft Office\\Office12\\",
          "10":"Microsoft Office\\Office14\\",
          "13":"Microsoft Office\\Office15\\"}

dict_last = {"doc":"WINWORD.EXE",
             "docx":"WINWORD.EXE",
             "xls":"EXCEL.EXE",
             "xlsx":"EXCEL.EXE",
             "ppt":"POWERPNT.EXE",
             "pptx":"POWERPNT.EXE",
             "inp":"InPage 2012.exe"}

for dir in os.listdir(vm_path):
    if dir == "winxp x86":continue
    if not os.path.isdir(vm_path):continue
    vmx_path = "\""+path+os.sep+dir+os.sep+dir+".vmx\""
    direct_output = subprocess.check_output("vmrun.exe listSnapshots " + vmx_path, shell=False)
    lst = direct_output.split("\r\n")[1:]
    
    for snap_name in lst:
	if 'update' in snap_name:continue
	if 'raw' in snap_name:continue
	if  len(snap_name) == 0:continue
	line = snap_name.replace("_","")
	c=vm_chk(line)
	os.system("vmrun.exe revertToSnapshot "+ vmx_path+ " "+ snap_name)
	os.system("vmrun.exe start "+ vmx_path)		    
	proc_lst_1 = subprocess.check_output('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123  listProcessesInGuest '+ vmx_path, shell=False)
	proc_lst_1 = proc2list(proc_lst_1)
	
	for files in os.listdir('C:\\Users\\admin7\\Desktop\\working\\file test'):
	    file_ext = files.split(".")[1]
	    file_name =files.split(".")[0]
	    
	    a = [line[i:i+2] for i in range(0, len(line), 2)]
			    
	    if a[1] == "64" and a[4] == "86":
		app_path = dict_first["64-86"] + dict_middle[a[3]] + dict_last[file_ext]
	    else:
		app_path = dict_first["86-86"] + dict_middle[a[3]] + dict_last[file_ext]
		
	    os.system('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123 CopyFileFromHostToGuest '+ vmx_path +' "C:\\Users\\admin7\\Desktop\\working\\file test\\'+files+'" "C:\\Users\\'+dir+'\\Desktop\\'+files+'"')
	    #print 'vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123 runProgramInGuest '+ vmx_path + ' -activeWindow -interactive '+ ' "'+app_path + '" "C:\\Users\\'+dir+'\\Desktop\\'+files+'"'
	    subprocess.Popen('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123 runProgramInGuest '+ vmx_path + ' -activeWindow -interactive '+ ' "'+app_path + '" "C:\\Users\\'+dir+'\\Desktop\\'+files+'"')
	    flag = False

	    for i in range(1,10):
		print "pass:- "+str(i)
		proc_lst_2 = subprocess.check_output('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123  listProcessesInGuest '+ vmx_path, shell=False)
		proc_lst_2 = proc2list(proc_lst_2)
		diff = tuple(set(proc_lst_2) - set(proc_lst_1))	
		for proc in diff:
		    print proc + " " + file_name.split("_")[1] + " ("+ str(proc.find(file_name.split("_")[1])) + ")" 
		    if proc.find(file_name.split("_")[1]) > 0:
			flag = True
			break
		if flag == True:break
		time.sleep(5)
	    fl = open("result.txt","a")
	    if flag == True:	
		os.system('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123 captureScreen '+ vmx_path + ' "C:\\Users\\admin7\\Desktop\\sc\\'+ dir + ' '+ snap_name +' '+ files + '.jpg"')
		fl.write(file_name + " "+ c + " working\n")
		print file_name + " "+ c + " working"
		print diff
	    else:
		fl.write(file_name + " "+ c + " not working\n")
		print file_name + " " + c + " not working"
		print diff		    
	    fl.close()   
	    
	    os.system("vmrun.exe revertToSnapshot "+ vmx_path+ " "+ snap_name)	  	
	    os.system("vmrun.exe start "+ vmx_path)			  
    os.system("vmrun.exe suspend "+ vmx_path)
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  	
			  		   
			       
		#if files.split(".")[1] == "doc"or"docx" and dir.split(" ")[1] == "x64":
	   
		   #os.system('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123 CopyFileFromHostToGuest '+ vmx_path + ' "C:\\Users\\admin7\\Desktop\\working\\file test\\'+files+'" "C:\\Users\\'+dir+'\\Desktop\\'+files+'"')   #copy
		   #os.system('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123 runProgramInGuest '+ vmx_path + ' -activeWindow -interactive '+' "C:\\Program Files (x86)\\Microsoft Office\\Office12\\WINWORD.EXE"  "C:\\Users\\'+dir+'\\Desktop\\'+files+'"')		    
		   #time.sleep(10)	       
		   #proc_lst_2 = subprocess.check_output('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123  listProcessesInGuest '+ vmx_path, shell=False)
		   #proc_lst_2 = proc_lst_2.split("\r\n")[1:]
		   #lst_2 = []
		   
		   #for pl in proc_lst_2:
		       #row = pl.split(",")
		       #if len(row) > 1:
			   #lst_2.append(row[0].replace("pid=","") + "-" + row[2].replace("cmd=","").replace("[","").replace("]","").strip())      
		  
		   #dif = tuple(set(lst_2) - set(lst_1))
		   
		   #if dif == 0:
		       #print "no anny exe "			  
		   
		   #if dif > 2:
		       #print dif
		       #print "find new exe "
		       #os.system('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123 captureScreen '+ vmx_path + ' "C:\\Users\\admin7\\Desktop\\'+ dir + ' '+ files + '.jpg"')
		       #print "screen short " + dir + ' '+ files + '.jpg"'
		       #os.system("vmrun.exe revertToSnapshot "+ vmx_path+ " "+ snap_name) 
		       #print "run new file "
		       #os.system("vmrun.exe start "+ vmx_path)
		       
				
	       
		      
		      
		      
		      
		       ##xls file		
		       #if files.split(".")[1] == "xls" and dir.split(" ")[1] == "x86":
		       ##copy    
			  #os.system('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123 CopyFileFromHostToGuest '+ vmx_path + ' "C:\\Users\\admin7\\Desktop\\working\\file test\\'+files+'" "C:\\Users\\'+dir+'\\Desktop\\'+files+'"')   #copy
		       ##run
			  #os.system('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123 runProgramInGuest '+ vmx_path + ' -activeWindow -interactive '+ ' "C:\\Program Files\\Microsoft Office\\Office12\\EXCEL.EXE"  "C:\\Users\\'+dir+'\\Desktop\\'+files+'"')
			 
		       #if files.split(".")[1] == "xls" and dir.split(" ")[1] == "x64":
		       ##copy    
			  #os.system('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123 CopyFileFromHostToGuest '+ vmx_path + ' "C:\\Users\\admin7\\Desktop\\working\\file test\\'+files+'" "C:\\Users\\'+dir+'\\Desktop\\'+files+'"')   #copy
		       ##run
			  #os.system('vmrun.exe -T ws -gu "'+dir +'" '+ '-gp 123 runProgramInGuest '+ vmx_path + ' -activeWindow -interactive '+ ' "C\\Program Files (x86)\\Microsoft Office\\Office12\\EXCEL.EXE"  "C:\\Users\\'+dir+'\\Desktop\\'+files+'"')		    
		       
