from app import create_app

system = create_app()

while True:

    try:
        query = input("\nquery>>> ")

    except KeyboardInterrupt:
        break

    if not query or query.lower in ("!quit", "!exit"):
        break

    context = system.run(query)

    print(f"\nresponse >>> {context.final_result}")

