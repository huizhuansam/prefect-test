from prefect import flow


@flow
def hello():
    print(f"Hello, Prefect! 🙌")
