from prefect import flow


@flow
def setup():
    print("Setting up...")

@flow
def hello():
    setup()
    print(f"Hello, Prefect! 🙌")

if __name__ == "__main__":
    hello()
    