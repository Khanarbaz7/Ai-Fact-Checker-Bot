# main.py
from fact_checker_bot.src.fact_checker import fact_check_claim

if __name__ == "__main__":
    claim = input("Enter a claim to fact-check: ")
    result = fact_check_claim(claim)

    print("\n=== FACT-CHECK REPORT ===")
    print(f"Claim: {result['claim']}")
    print(f"\nInitial Answer: {result['initial_answer']}")

    print("\nAssumptions & Verification:")
    for r in result["assumptions"]:
        print(f"- Assumption: {r['assumption']}")
        print(f"  Verification: {r['verification']}")
        print(f"  Evidence:\n    {r['evidence']}\n")

    print(f"\nFinal Answer: {result['final_answer']}")
