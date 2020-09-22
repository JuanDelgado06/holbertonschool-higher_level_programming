#!/usr/bin/python3
def safe_function(func, *args):
    import sys
    try:
        return func(*args)
    except Exception as e:
        print("Exception: " + str(e), file=sys.stderr)
        return None
