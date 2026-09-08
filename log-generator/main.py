import logging
import random
import time


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("test-app")


INFO_MESSAGES = [
    "User successfully authenticated",
    "Request processed successfully",
    "Background task completed",
    "Cache updated",
    "Worker is running",
]

WARNING_MESSAGES = [
    "High memory usage detected",
    "Slow database response",
    "Retrying external request",
    "Cache miss rate is high",
]

ERROR_MESSAGES = [
    "Database connection failed",
    "Failed to process request",
    "Connection to Redis refused",
    "Internal application error",
    "Payment service unavailable",
]


def generate_log():
    log_type = random.choice(["info", "info", "info", "warning", "error"])

    if log_type == "info":
        logger.info(random.choice(INFO_MESSAGES))

    elif log_type == "warning":
        logger.warning(random.choice(WARNING_MESSAGES))

    elif log_type == "error":
        logger.error(random.choice(ERROR_MESSAGES))


def main():
    logger.info("Test log generator started")

    while True:
        generate_log()
        time.sleep(3)


if __name__ == "__main__":
    main()
