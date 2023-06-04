import PySimpleGUI as sg
g=['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack', 'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3','GrayGrayGray']
ip_address='127.0.0.1'
sg.theme("Gray Gray Gray")
layout = [[sg.Text('Website Blocker',justification="c",font="Arial 20")]
          ,[sg.Text('Enter website url'),sg.Input(key="-url-")],
          [sg.Button('Block',key='-block-'),sg.Text("    "),sg.Button("Unblock",key='-unblock-'),sg.Text("    "),
           sg.Button("Exit",key="-exit-")]]
window=sg.Window("Url Blocker",layout,element_justification="c",size=[500,300],font='Arial 12',icon="icon.ico")
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED or event=="-exit-":
        break                        
    if event == "-block-":
        url=values["-url-"]
        with open('C:\Windows\System32\drivers\etc\hosts','r+') as host_file:
            file_content= host_file.read()
            if url in file_content:
                sg.Popup("Already Blocked")
            else:
                host_file.write(ip_address+' '+url+'\n')
                sg.Popup("BLOCKED")

    if event == "-unblock-":
        url=values["-url-"]
        url1=ip_address+' '+url+'\n'
        with open('C:\Windows\System32\drivers\etc\hosts','r+') as host_file:
            line=host_file.readlines()
            print(line)
            if url1 in line:
                print(url1)
                line.remove(url1)
                sg.Popup("UNBLOCKED")
                print(line)
                host_file.close()
                host_file=open('C:\Windows\System32\drivers\etc\hosts','w')
                for li in line:
                    host_file.write(li)

                host_file.close()
            else:
                sg.Popup("Already UNBLOCKED")
        sg.Popup(url,"is unblocked")

window.close()
