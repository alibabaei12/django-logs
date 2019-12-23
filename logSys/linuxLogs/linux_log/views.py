from django.shortcuts import render
from . import ssh
from .models import Folder, File

def home(request):
    return render(request, "index.html")

def connect_page(request):
    return render(request, "connect_page.html")


connection : ssh.Ssh
logs: list
file_name: str
def log_files(request):

    #get the credesials to ssh 
    hostname= request.POST["hostname"]
    username = request.POST["username"]
    password = request.POST["password"]
    
    global connection
    connection = ssh.Ssh(hostname, username, password)
    
    
    # print("the path is: " , connection.path)
    files_folders = connection.getFile_folders()
    
    files=[]
    for i in files_folders:
        if i.tp == "file_type":
            files.append(i)
    # file_type = type(File)
    # folder_type = type(Folder)

    # print("File type is: " , file_type)
    # print("folder type is: " , folder_type)

    if connection != None:
        path = connection.path
        return render(request, "log_files.html", {"path": path, "files": files})
    
    else:
        return render(request, "index.html", {"path": "No Connection"})
    
def cd_folder(request):

    folder_name = request.POST["folder_name"]
    # print("folder name is: ", folder_name)
    
    files_folders = connection.cd(folder_name)
    
    path = connection.path
    # print ("the list is: " , files_folders)
    return render(request, "log_files.html", {"path": path, "files": files})

def file_view(request):
    

    if 'file_name' in request.GET:
        global file_name
        file_name = request.GET["file_name"]
        global logs
        logs = connection.readFiles(file_name)

    

# filter(lambda k: 'ab' in k, lst)
# lst = ['a', 'ab', 'abc', 'bac']
# >>> res = [k for k in lst if 'ab' in k]
    search_term= ''

    if 'search' in request.GET:
        search_term = request.GET["search"]
        if search_term != '':
            print("searchterm is: " , search_term)
            logs = [x for x in logs if search_term in x]
        else:
            logs = connection.readFiles(file_name)
    # print("logs areeee: ", logs)
    print("the logs areeee: " , logs)
    return render(request, "file_view.html", {"logs": logs, "search_term":search_term})
