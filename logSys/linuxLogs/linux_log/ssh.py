import paramiko
from .models import File, Folder
class Ssh:

    hostname: str
    username: str
    password: str
    connection = None
    path: str
    files_folders: list


    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.connection = paramiko.SSHClient()
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.path = "/var/log"
        self.connection.connect(hostname="35.223.103.101", username="alibabaei12", password="Amirbaba12345")
        self.files_folders = []



    def getFile_folders(self):

        stdin, stdout, stderr = self.connection.exec_command("cd /var/log ; ls -l")

        stdout = stdout.readlines()

        # print("the pwd comment returns: " + str(stdout))
        st = None
        # see if its a file or folder and get the name as well
        for i in stdout:
            st = i.split(" ")
            name = st[len(st) - 1]
            name = name[0: len(name)-1]
            # print("the name isssss: " + name)
            if st[0][0] == 'd':
                folder = Folder(name, self.path)

                self.files_folders.append(folder)
                
            elif st[0][0] == '-':
                file = File(name,self.path, "empty")

                self.files_folders.append(file)
        
        return self.files_folders


    def pwd(self):

        cmd_pwd = "pwd"
        if self.connection != None:
            stdin,stdout,stderr = self.connection.exec_command(cmd_pwd)

            stdout = stdout.readlines()
            # print("cccc" ,stdout)
            clean = str(stdout)
            self.path = clean[2:len(clean)-4]
            self.init_path = self.path
            # print("initial path: " + self.path)
            clean = "Current Location is: " + clean[2:len(clean)-4]
            # print("path after cleaning: " , clean)
            return self.path
        else:
            return None

    def cd(self, folder_name):
        
        # print("the path in the beginning of the cd page is: " , self.path)
        self.path = "/var/log"
        self.files_folders.clear()
        self.path += ("/" + folder_name)
        # print("the cd path is; " + self.path + " ; ls -l")
        stdin, stdout, stderr = self.connection.exec_command("cd " + self.path + " ; ls -l")

        stdout= stdout.readlines()
        # print("the stdout is " + str(stdout))
        # print ( "the error is: " + str(stderr) )
        for i in stdout:
            st = i.split(" ")
            name = st[len(st) - 1]
            if st[0][0] == 'd':
                folder = Folder(name, self.path)
                self.files_folders.append(folder)
            elif st[0][0] == '-':
                file = File(name, self.path,"empty")
                self.files_folders.append(file)

        # print("currrr is : " + self.currentPath)
        # stdin, stdout, stderr = self.hp.exec_command("pwd")
        # stdout = stdout.readlines()
        # print("worrkkkk " + str(stdout))
        return self.files_folders

    def readFiles(self,file_name):
        
        self.path += ("/" + file_name)
        # print("the cd path is; " + self.path )
        stdin, stdout, stderr = self.connection.exec_command("sudo cat " + self.path )

        stdout = stdout.readlines()
        
        # print("stdout issss:     " , stdout)
        self.path = "/var/log"
        return stdout