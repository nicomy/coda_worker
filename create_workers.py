# import yaml
from ruamel import yaml
import io
import sys
import os
import shutil


nb_workers_deploy = 3

print("Script Name:", sys.argv[0])  # Name of the script
if len(sys.argv) > 1:
    print("Arguments:", sys.argv[1:])  # List of arguments
    nb_workers_deploy =sys.argv[1:]
else:
    print("No arguments passed. Using default number of workers :", nb_workers_deploy)



template_path= "template_worker"
docker_file_source = "docker-compose.yml" 



for current_worker in range(nb_workers_deploy):
    target_path = "worker"+str(current_worker)+"/"
    shutil.copytree(template_path,target_path , dirs_exist_ok=True)
    os.chdir(target_path)

    docker_compose_file =  docker_file_source
    print(docker_compose_file)
    # Read YAML file
    with open(docker_compose_file, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    data_loaded["services"]["worker"]["container_name"] =   data_loaded["services"]["worker"]["container_name"]+str(current_worker)

    with io.open(docker_compose_file, 'w', encoding='utf8') as outfile:
        yaml.dump(data_loaded, outfile, default_flow_style=False, allow_unicode=True)


    os.chdir("..")

    



