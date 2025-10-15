key_hex = "9C2BAB97BCF8C0C4F1A9EA7881A213F6C9EBF9D8D4C6A8E43CE5A259BDE7E9FD"

def apply_encryption(db, **kwargs):
    """You must include an argument for keying, and optional cipher configurations"""

    if db.in_transaction:
        raise Exception("Won't update encryption while in a transaction")

    # the order of pragmas matters
    def pragma_order(item):
        # pragmas are case insensitive
        pragma = item[0].lower()
        # cipher must be first
        if pragma == "cipher":
            return 1
        # old default settings reset configuration next
        if pragma == "legacy":
            return 2
        # then anything with legacy in the name
        if "legacy" in pragma:
            return 3
        # all except keys
        if pragma not in {"key", "hexkey", "rekey", "hexrekey"}:
            return 3
        # keys are last
        return 100

    # check only ome key present
    if 1 != sum(1 if pragma_order(item) == 100 else 0 for item in kwargs.items()):
        raise ValueError("Exactly one key must be provided")

    for pragma, value in sorted(kwargs.items(), key=pragma_order):
        # if the pragma was understood and in range we get the value
        # back, while key related ones return 'ok'
        expected = "ok" if pragma_order((pragma, value)) == 100 else str(value)
        if db.pragma(pragma, value) != expected:
            raise ValueError(f"Failed to configure {pragma=}")

    # Try to read from the database.  If the database is encrypted and
    # the cipher/key information is wrong you will get NotADBError
    # because the file looks like random noise
    db.pragma("quick_check")