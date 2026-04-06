from typing import Dict


class ResponseComparator:

    @staticmethod
    def display(results: Dict[str, str]):
        print("\n" + "=" * 60)
        print("🧠 Multi-LLM Comparison Results")
        print("=" * 60)

        for model, response in results.items():
            print(f"\n🔹 {model}")
            print("-" * 60)
            print(response)

        print("\n" + "=" * 60 + "\n")
