import docker
import time
import traceback


def main():
    print("=== LOG READER STARTED ===", flush=True)

    try:
        print("Connecting to Docker...", flush=True)

        client = docker.from_env()

        print("Connected to Docker!", flush=True)

        while True:
            print("Scanning containers...", flush=True)

            containers = client.containers.list(
                filters={
                    "label": "fixops.enabled=true"
                }
            )

            print(
                f"Found {len(containers)} target container(s)",
                flush=True
            )

            for container in containers:
                print(
                    f"Container: {container.name}",
                    flush=True
                )

                logs = container.logs(
                    tail=10,
                    timestamps=True,
                ).decode(
                    "utf-8",
                    errors="replace"
                )

                for line in logs.splitlines():
                    if "ERROR" in line.upper():
                        print(
                            f"[FOUND ERROR] {line}",
                            flush=True
                        )
                    else:
                        print(
                            f"[LOG] {line}",
                            flush=True
                        )

            print("Waiting 3 seconds...\n", flush=True)

            time.sleep(3)

    except Exception:
        print("!!! READER ERROR !!!", flush=True)
        traceback.print_exc()


if __name__ == "__main__":
    main()
