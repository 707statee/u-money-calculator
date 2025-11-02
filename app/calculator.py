from typing import List, Dict


class Ledger:
    """Класс для ведения учёта доходов и расходов."""

    def __init__(self):
        self.entries: List[Dict] = []

    def add_income(self, amount: float, description: str = "") -> None:
        if amount <= 0:
            raise ValueError("Amount must be > 0")
        self.entries.append({"type": "income", "amount": float(amount), "description": description})

    def add_expense(self, amount: float, description: str = "") -> None:
        if amount <= 0:
            raise ValueError("Amount must be > 0")
        self.entries.append({"type": "expense", "amount": float(amount), "description": description})

    def balance(self) -> float:
        total = 0.0
        for e in self.entries:
            if e["type"] == "income":
                total += e["amount"]
            else:
                total -= e["amount"]
        return total

    def summary(self) -> Dict[str, float]:
        income = sum(e["amount"] for e in self.entries if e["type"] == "income")
        expense = sum(e["amount"] for e in self.entries if e["type"] == "expense")
        return {"income": income, "expense": expense, "balance": income - expense}


if __name__ == "__main__":
    ledger = Ledger()
    ledger.add_income(1000, "Salary")
    ledger.add_expense(200, "Food")
    print("Balance:", ledger.balance())
    print("Summary:", ledger.summary())
