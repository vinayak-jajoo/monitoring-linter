def generate_report(errors, warnings, info):
    print("\n--- LINT REPORT ---\n")

    if errors:
        print("ERRORS:")
        for e in errors:
            print(f" - {e}")

    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(f" - {w}")

    if info:
        print("\nINFO:")
        for i in info:
            print(f" - {i}")

    if not (errors or warnings or info):
        print("No issues found!")

    print("\n-------------------\n")