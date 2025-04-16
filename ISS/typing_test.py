from typing import List, Dict, Optional

def greet(name: str) -> str:
    return f"Hello, {name}!"

def process_data(data: List[Dict[str, Optional[int]]]) -> List[int]:
    return [x["value"] for x in data if x.get("value") is not None]

# Test
print(greet("Alice"))  # Should print: "Hello, Alice!"

data = [{"value": 10}, {"value": None}, {"value": 20}]
print(process_data(data))  # Should print: [10, 20]