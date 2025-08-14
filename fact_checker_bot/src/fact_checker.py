# fact_checker_bot/src/fact_checker.py
from fact_checker_bot.src.prompt_chains import initial_response, extract_assumptions, verify_assumption, final_synthesis
import logging
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/fact_checks.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fact_check_claim(claim: str):
    try:
        # Step 1: Initial answer
        answer = initial_response(claim)

        # Step 2: Extract assumptions
        assumptions = extract_assumptions(answer)
        if not assumptions:
            assumptions = [answer] 

        # Step 3: Verify each assumption
        results = []
        for assumption in assumptions:
            if assumption.strip():
                verification_result = verify_assumption(assumption.strip())
                results.append(verification_result)

        # Step 4: Final synthesis
        final_answer = final_synthesis(claim, results)

        # Log the fact-check
        logging.info(
            "Claim: %s | Initial Answer: %s | Final Answer: %s | Assumptions: %s",
            claim,
            answer,
            final_answer,
            results
        )

        return {
            "claim": claim,
            "initial_answer": answer,
            "assumptions": results,  # list of dicts from verify_assumption()
            "final_answer": final_answer
        }

    except Exception as e:
        logging.error("Error processing claim '%s': %s", claim, str(e))
        raise

if __name__ == "__main__":
    claim = input("Enter a claim to fact-check: ")
    result = fact_check_claim(claim)

    print("\n=== FACT-CHECK REPORT ===")
    print(f"Claim: {result['claim']}")
    print(f"\nInitial Answer: {result['initial_answer']}")
    print("\nAssumptions & Verification:")
    for r in result["assumptions"]:
        print(f"- Assumption: {r['assumption']}")
        print(f"  Verdict: {r['verdict']} — {r['explanation']}")
        if r.get("evidence_links"):
            print("  Evidence Links:")
            for link in r["evidence_links"]:
                print(f"    - {link}")

    print(f"\nFinal Answer: {result['final_answer']}")

