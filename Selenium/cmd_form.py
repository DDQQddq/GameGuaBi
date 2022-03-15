import os


def command(p, con_p):
    try:
        _dir = "D://selenium//" + con_p
        command1 = "cd C://Program Files//Google//Chrome//Application//"
        command2 = "chrome.exe --remote-debugging-port=" + p + " --user-data-dir=" + _dir
        cmd = command1 + '&&' + command2
        os.popen(cmd)

    except Exception as e:
        print("cloc tool fail" + str(e))
