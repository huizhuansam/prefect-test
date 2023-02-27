from prefect import flow


@flow
def setup():
    print("Setting up...")

@flow
def hello(log_prints=True):
    setup()
    print(f"Hello, Prefect! 🙌")

if __name__ == "__main__":
    hello()
