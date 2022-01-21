import ftplib,os

localpath="/home/kali/abiral"
remotepath="/home/kali/Desktop"
conn=ftplib.FTP('10.0.2.15')
conn.login("kali","kali")
conn.cwd(remotepath)
root=conn.nlst()

def downloadOne(remotefile):
    file=open(os.path.join(localpath,remotefile),"wb")
    conn.retrbinary("RETR "+remotefile,file.write)

def scraper(content_path):
    folder=conn.nlst()
    for content_name in folder:
        conn.cwd(content_path)
        try:
            conn.cwd(content_name) 
            scraper(os.path.join(content_path,content_name)) #don't use veriable to store path if done the previous callback will use the save path and won't find the file

        except:
            downloadOne(content_name)


for content_name in root:
    conn.cwd(remotepath)
    try:
        conn.cwd(content_name)
        content_path=os.path.join(remotepath,content_name)
        scraper(content_path)
    except:
        downloadOne(content_name)
