import docker

def get_container_name(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    container_name = container.name
    return container_name

# Specify the container ID
container_id = "your-container-id"

# Get the container name
container_name = get_container_name(container_id)

print(f"Container Name: {container_name}")
