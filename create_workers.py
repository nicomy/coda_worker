from ruamel.yaml import YAML
import io
import sys
import os
import shutil

nb_workers_deploy = 3

print("Script Name:", sys.argv[0])
if len(sys.argv) > 1:
    print("Arguments:", sys.argv[1:])
    nb_workers_deploy = int(sys.argv[1])
else:
    print("No arguments passed. Using default number of workers:", nb_workers_deploy)

template_path = "template_worker"
docker_file_source = "docker-compose.yml"

# Create a YAML loader instance
yaml = YAML(typ='safe')  # ‘safe’ type, same as old safe_load

for current_worker in range(nb_workers_deploy):
    target_path = f"worker{current_worker}/"
    shutil.copytree(template_path, target_path, dirs_exist_ok=True)
    os.chdir(target_path)

    docker_compose_file = docker_file_source
    print(docker_compose_file)

    # Read YAML file
    with open(docker_compose_file, 'r') as stream:
        data_loaded = yaml.load(stream)

    # Modify the container name
    data_loaded["services"]["worker"]["container_name"] += str(current_worker)

    # Write back to YAML file
    with io.open(docker_compose_file, 'w', encoding='utf8') as outfile:
        yaml.dump(data_loaded, outfile)

    os.chdir("..")


    



