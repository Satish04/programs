"""This program has overlapping() function that takes two lists and returns True if they have at least one member in common, 
False otherwise."""

def overlapping(ip_List1, ip_List2):
 
    print (ip_List1)
    print (ip_List2)
     
    for i in range(len(ip_List1)):
         
        for j in range(len(ip_List2)):
 
            if ip_List1[i] == ip_List2[j]:
                return True
             

if __name__ == "__main__":
	List1 = ['aa','bb','cc']
	List2 = ['cc','dd','ee']
	if overlapping(List1,List2) == True:
		print 'True'
	else:
		print 'False'







   