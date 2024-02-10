import os,httpx        
approval():
	frist="=["
	last="]="
	uuid=str(os.getuid()) + str(os.getlogin())
	key = "6".join(uuid)
	ress=httpx.get("").text
	if key in ress:
		main()
	else:
		print("YOUR KEY IS NOT APPROVED")
		os.system("clear")
		print("THIS TOOL.IS FREE BUT YOU NEED PERMITION TO USE IT")
		print("Your key : "+frist+key+last)
		print("=======================")
		name = input("YOUR NAME ")
		os.system("xdg-open https://wa.me/+8801863713434")         