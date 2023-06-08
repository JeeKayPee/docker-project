import subprocess

def get_container_name(container_id):
    cmd = f"docker inspect --format='{{{{.Name}}}}' {container_id}"
    result = subprocess.check_output(cmd, shell=True, text=True)
    container_name = result.strip('/')
    return container_name

# Specify the container ID
container_id = "your-container-id"

# Get the container name
container_name = get_container_name(container_id)

print(f"Container Name: {container_name}")
