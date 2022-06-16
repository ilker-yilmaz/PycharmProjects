import os
import win32com.client

ppttoPDF = 32

for root, dirs, files in os.walk(r'C:/Users/eymen/Desktop/Girişimcilik-I/belgeler'):
    for f in files:

        if f.endswith(".pptx"):
            try:
                print(f)
                in_file=os.path.join(root,f)
                powerpoint = win32com.client.Dispatch("Powerpoint.Application")
                deck = powerpoint.Presentations.Open(in_file)
                deck.SaveAs(os.path.join(root,f[:-5]), ppttoPDF) # formatType = 32 for ppt to pdf
                deck.Close()
                powerpoint.Quit()
                print('done')
                os.remove(os.path.join(root,f))
                pass
            except:
                print('could not open')
                # os.remove(os.path.join(root,f))
        elif f.endswith(".ppt"):
            try:
                print(f)
                in_file=os.path.join(root,f)
                powerpoint = win32com.client.Dispatch("Powerpoint.Application")
                deck = powerpoint.Presentations.Open(in_file)
                deck.SaveAs(os.path.join(root,f[:-4]), ppttoPDF) # formatType = 32 for ppt to pdf
                deck.Close()
                powerpoint.Quit()
                print('done')
                os.remove(os.path.join(root,f))
                pass
            except:
                print('could not open')
                # os.remove(os.path.join(root,f))
        else:
            pass