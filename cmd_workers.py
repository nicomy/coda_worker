import sys
import os
import subprocess


nb_workers_deploy = 3
cmd = "up"


# print("Script Name:", sys.argv[0])  # Name of the script
if len(sys.argv) > 2 :
    # print("Arguments:", sys.argv[1:])  # List of arguments
    nb_workers_deploy =int(sys.argv[1])
    cmd =sys.argv[2]
elif len(sys.argv) > 1  :
    # print("Arguments:", sys.argv[1:])  # List of arguments
    nb_workers_deploy =int(sys.argv[1])
    # cmd =sys.argv[2]
else:
    print("No arguments passed. Using default number of workers :", nb_workers_deploy)

print("running script with parameteers : ", nb_workers_deploy, cmd)


dic_cmd_to_real_cmd = {
    "up" : "sudo docker compose up -d ",
    "down" : "sudo docker compose down",
    "logs" : "sudo docker compose logs"
}




for current_worker in range(nb_workers_deploy):

    target_path = "worker"+str(current_worker)+"/"
    # shutil.copytree(template_path,target_path )
    os.chdir(target_path)
    subprocess.run(dic_cmd_to_real_cmd[cmd], shell=True) 

    os.chdir("..")



#if lock : sudo aa-remove-unknown
