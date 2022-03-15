import cmd_form

port = input("请输入端口号（5003/5004）: ")
if int(port) == 5003:
    con_port = "auto"
else:
    con_port = port

cmd_form.command(port, con_port)
