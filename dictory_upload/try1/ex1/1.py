import os
def copy_afile(src_path,dest_path):
    with open(src_path) as src, open(dest_path,'w') as dest:
        src = src.read()
        dest.write(src.upper())
def one_level(folder_path):
    try:
        os.makedirs(to_server_folder+folder_path)
    except OSError as e:
        if e.errno == 17:  
            pass    
def folder_copy(key,str_var):
    folder_path=""
    source_path = "c:\\server_folder\\"+key
    destination_path = to_server_folder+ str_var.replace("/","\\")
    print("The source_path ={}".format(source_path))
    print("The destination_path ={}".format(destination_path))
    while str_var.find('/') != -1:
        folder_path = folder_path+"\\"+str_var[0:str_var.find('/')]
        one_level(folder_path) 
        str_var = str_var[str_var.find('/')+1:]
    copy_afile(source_path,destination_path)
to_server_folder = "c:\\xcopy\\"
dict1 = {"1.py":"try1/1.py","2.py":"try1/2.py","3.py":"try1/try2/3.py","4.py":"try1/try2/4.py"}
keys  = list(dict1)
for key in keys:
    folder_copy(key,dict1.get(key))
