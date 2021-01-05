
import platform
import subprocess

def ping(host):
    """

    :param host: IP address
    :return: Active or not
    """
    ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if platform.system().lower() == "windows" else True
    # Ping
    return subprocess.call(args, shell=need_sh) == 0


def check_software():
    """

    :param software: software name
    :return: True or False
    """
    #
    if platform.system().lower() == "windows":
        software_names = subprocess.check_output(["wmic","product","get","name"])
        software_names = str(software_names)
        try:
            # arrange the string
            for i in range(len(software_names)):
                print(software_names.split("\\r\\r\\n")[6:][i])
        except IndexError as e:
            print("All Done")
    else:
        software_names = subprocess.check_output(['rpm', '-qa'])
        for package in software_names.split('\n'):
            print(package)


# Ping and check whether Ip iis active or not
print(ping("192.168.17.142"))

# Checking all Installed Software
check_software()