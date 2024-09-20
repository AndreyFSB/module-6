def is_valid(value: str) -> bool:
    acc = []
    brackets = ("()", "[]", "{}")
    for ch in value:
        for br in brackets:
            if ch == br[0]:
                acc.append(br[0])
            elif ch == br[1]:
                if not acc or acc[-1] != br[0]:
                    return False
                acc.pop()
    return len(acc) == 0
