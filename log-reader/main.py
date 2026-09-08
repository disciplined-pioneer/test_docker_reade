import docker


def main():
    client = docker.from_env()

    print("Log Reader started")
    print("Looking for containers with label: fixops.enabled=true")
    print()

    while True:
        containers = client.containers.list(
            filters={
                "label": "fixops.enabled=true"
            }
        )

        for container in containers:
            print(f"--- Reading logs from: {container.name} ---")

            logs = container.logs(
                tail=20,
                timestamps=True,
            ).decode("utf-8", errors="replace")

            for line in logs.splitlines():
                if "ERROR" in line.upper():
                    print(f"[FOUND ERROR] {line}")
                else:
                    print(f"[LOG] {line}")

            print()


if __name__ == "__main__":
    main()
