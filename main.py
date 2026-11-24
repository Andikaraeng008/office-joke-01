import os

TEXT = "HR said we are a family, so I asked why the family reunion is a performance review."

def main():
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "gate: 1-200 chars, not whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
