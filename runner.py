# runner.py
from fact_checker_bot.src.fact_check_service import fact_check

def run_cli():
    while True:
        claim = input("\nEnter a claim to fact-check (or 'q' to quit): ")
        if claim.lower() in ["q", "quit", "exit"]:
            break
        
        result = fact_check(claim)

        print("\n=== FACT-CHECK REPORT ===")
        print(f"Claim: {result['claim']}")
        print(f"\nInitial Answer: {result['initial_answer']}\n")

        print("Assumptions & Verification:")
        for r in result['assumptions']:
            print(f"- Assumption: {r['assumption']}")
            print(f"  Verdict: {r.get('verdict', 'N/A')}")
            print(f"  Explanation: {r.get('explanation', '')}")
            if r.get('evidence_links'):
                print(f"  Evidence Links:")
                for link in r['evidence_links']:
                    print(f"    • {link}")

        print("\nFinal Answer:", result['final_answer'])
        print("="*50)

if __name__ == "__main__":
    run_cli()
