from memory.fact_memory import FactMemory

def test_set_fact():

    memory = FactMemory()

    memory.set_fact(
        "favorite_city",
        "Pune"
    )

    assert (
        memory.get_fact(
            "favorite_city"
        )
        == "Pune"
    )