# Code by Jaicob Remon

# Importing dropbox
import dropbox

#Creating class transferdata
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    #Defining upload file function
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    #Giving access token
    access_token = 'sl.BFKqmdzZr3Nsqzqe_m7UrDVrlXRNWxaD5WAFNucdKGcDcttag5iAPXwoIzctQC0e0KufEoQrcwhiZ-kj8BAQJ2urXubTxynzJh10iA6pOmLK7a-m1PwLUSBCWKHRFPdU0TCAywGpKn_J'
    transferData = TransferData(access_token)

    #Asking for file path and new name of file
    print("Welcome to backup software version 1.0 !")
    file_from = input("Enter the file path to transfer !: -")
    file_to = input("Enter the new name of the file !:- ")  

    #Uploading the file and telling user it has been uploaded
    transferData.upload_file(file_from, file_to)
    print("file has been moved ! Check your dropbox to see your file !")
    print("☻")

#Initializing main function
main()



