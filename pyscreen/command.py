import subprocess

def command(command,final_line=None,cwd=None, return_output = False):

    if isinstance(command,str):
        command = command.split()

    if cwd == None:
        popen = subprocess.Popen(command, stdout=subprocess.PIPE)
    else:
        popen = subprocess.Popen(command, stdout=subprocess.PIPE,cwd=cwd)

    lines_iterator = iter(popen.stdout.readline, b"")
    output = None

    for line in lines_iterator:

        if return_output:
            if output == None:
                output = [line]
            else:
                output.append(line)
        else:
            print(line)

        if final_line != None and final_line in str(line):
            return output

    return output