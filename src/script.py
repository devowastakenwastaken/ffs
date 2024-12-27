import os, shutil

path = input('What directory would you like to sort? > ')
file_name = os.listdir(path)
folder_names = ['\\Data', '\\Images', '\\Apps', '\\Text', '\\Icons', '\\Videos', '\\Compressed files', '\\Audio', '\\Installers', '\\Desktop Themepacks', '\\Boot images (OS boot files)\\']

for loop in range(0, 11):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))

for file in file_name:
    if '.csv' in file and not os.path.exists(path + '\\Data\\' + file):
        shutil.move(path + '\\' + file, path + '\\Data\\' + file)
    elif '.xlsx' in file and not os.path.exists(path + '\\Data\\' + file):
        shutil.move(path + '\\' + file, path + '\\Data\\' + file)
    elif '.pdf' in file and not os.path.exists(path + '\\Data\\' + file):
        shutil.move(path + '\\' + file, path + '\\Data\\' + file)
    elif '.xls' in file and not os.path.exists(path + '\\Data\\' + file):
        shutil.move(path + '\\' + file, path + '\\Data\\' + file)
    elif '.json' in file and not os.path.exists(path + '\\Data\\' + file):
        shutil.move(path + '\\' + file, path + '\\Data\\' + file)
    
    elif '.exe' in file and not os.path.exists(path + '\\Apps\\' + file):
        shutil.move(path + '\\' + file, path + '\\Apps\\' + file)
        
    elif '.msi' in file and not os.path.exists(path + '\\Installers\\' + file):
        shutil.move(path + '\\' + file, path + '\\Installers\\' + file)
    elif 'Installer' in file and not os.path.exists(path + '\\Installers\\' + file):
        shutil.move(path + '\\' + file, path + '\\Installers\\' + file)
    elif '.pkg' in file and not os.path.exists(path + '\\Installers\\' + file):
        shutil.move(path + '\\' + file, path + '\\Installers\\' + file)
    elif '.deb' in file and not os.path.exists(path + '\\Installers\\' + file):
        shutil.move(path + '\\' + file, path + '\\Installers\\' + file)
    elif 'Setup' in file and not os.path.exists(path + '\\Installers\\' + file):
        shutil.move(path + '\\' + file, path + '\\Installers\\' + file)
    
        
    elif '.png' in file and not os.path.exists(path + '\\Images\\' + file):
        shutil.move(path + '\\' + file, path + '\\Images\\' + file)
    elif '.jpg' in file and not os.path.exists(path + '\\Images\\' + file):
        shutil.move(path + '\\' + file, path + '\\Images\\' + file)
    elif '.jpeg' in file and not os.path.exists(path + '\\Images\\' + file):
        shutil.move(path + '\\' + file, path + '\\Images\\' + file)
    elif '.webp' in file and not os.path.exists(path + '\\Images\\' + file):
        shutil.move(path + '\\' + file, path + '\\Images\\' + file)
    elif '.svg' in file and not os.path.exists(path + '\\Images\\' + file):
        shutil.move(path + '\\' + file, path + '\\Images\\' + file)
    elif '.avif' in file and not os.path.exists(path + '\\Images\\' + file):
        shutil.move(path + '\\' + file, path + '\\Images\\' + file)
        
    elif '.ico' in file and not os.path.exists(path + '\\Icons\\' + file):
        shutil.move(path + '\\' + file, path + '\\Icons\\' + file)
    
    elif '.iso' in file and not os.path.exists(path + '\\Boot images (OS boot files)\\' + file):
        shutil.move(path + '\\' + file, path + '\\Boot images (OS boot files)\\' + file)
    elif '.img' in file and not os.path.exists(path + '\\Boot images (OS boot files)\\' + file):
        shutil.move(path + '\\' + file, path + '\\Boot images (OS boot files)\\' + file)
    elif '.vhd' in file and not os.path.exists(path + '\\Boot images (OS boot files)\\' + file):
        shutil.move(path + '\\' + file, path + '\\Boot images (OS boot files)\\' + file)

    
    elif '.zip' in file and not os.path.exists(path + '\\Compressed files\\' + file):
        shutil.move(path + '\\' + file, path + '\\Compressed files\\' + file)
    elif '.rar' in file and not os.path.exists(path + '\\Compressed files\\' + file):
        shutil.move(path + '\\' + file, path + '\\Compressed files\\' + file)
    elif '.tar.gz' in file and not os.path.exists(path + '\\Compressed files\\' + file):
        shutil.move(path + '\\' + file, path + '\\Compressed files\\' + file)
    elif '.torrent' in file and not os.path.exists(path + '\\Compressed files\\' + file):
        shutil.move(path + '\\' + file, path + '\\Compressed files\\' + file)
        
    elif '.txt' in file and not os.path.exists(path + '\\Text\\' + file):
        shutil.move(path + '\\' + file, path + '\\Text\\' + file)
    elif '.rtt' in file and not os.path.exists(path + '\\Text\\' + file):
        shutil.move(path + '\\' + file, path + '\\Text\\' + file)
    elif '.md' in file and not os.path.exists(path + '\\Text\\' + file):
        shutil.move(path + '\\' + file, path + '\\Text\\' + file)
    
    elif '.mp4' in file and not os.path.exists(path + '\\Videos\\' + file):
        shutil.move(path + '\\' + file, path + '\\Videos\\' + file)
    elif '.mov' in file and not os.path.exists(path + '\\Videos\\' + file):
        shutil.move(path + '\\' + file, path + '\\Videos\\' + file)
    elif '.avi' in file and not os.path.exists(path + '\\Videos\\' + file):
        shutil.move(path + '\\' + file, path + '\\Videos\\' + file)
    
    elif '.mp3' in file and not os.path.exists(path + '\\Audio\\' + file):
        shutil.move(path + '\\' + file, path + '\\Audio\\' + file)
    elif '.wav' in file and not os.path.exists(path + '\\Audio\\' + file):
        shutil.move(path + '\\' + file, path + '\\Audio\\' + file)
    elif '.flac' in file and not os.path.exists(path + '\\Audio\\' + file):
        shutil.move(path + '\\' + file, path + '\\Audio\\' + file)
    elif '.m4a' in file and not os.path.exists(path + '\\Audio\\' + file):
        shutil.move(path + '\\' + file, path + '\\Audio\\' + file)
    elif '.ogg' in file and not os.path.exists(path + '\\Audio\\' + file):
        shutil.move(path + '\\' + file, path + '\\Audio\\' + file)
    elif '.aac' in file and not os.path.exists(path + '\\Audio\\' + file):
        shutil.move(path + '\\' + file, path + '\\Audio\\' + file)
    
    elif '.deskthemepack' in file and not os.path.exists(path + '\\Desktop Themepacks\\' + file):
        shutil.move(path + '\\' + file, path + '\\Desktop Themepacks\\' + file)
    
    else:
        print('Unable to move some files!')
 