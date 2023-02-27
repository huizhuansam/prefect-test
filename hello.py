from prefect import flow, get_run_logger


@flow
def add(x, y):
    return x + y

@flow
def setup():
    logger = get_run_logger()
    logger.info("Setting up...")
    logger.info(f"Addition result = {add(6, 7)}")

@flow
def hello(log_prints=True):
    setup()
    print(f"Hello, Prefect! 🙌")

if __name__ == "__main__":
    hello()
