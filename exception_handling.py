#!/usr/bin/env python
import os
from contextlib import suppress

values = [0, 5, 18, 0, 1, 47, 35, 0, 98, "123",]

for v in values:
    try:
        result = round(25 / v, 3)
    except ZeroDivisionError as err:
        print(err)
    except (TypeError, ValueError) as err:
        print(err)
    except Exception as err:
        print("Whoa!", err)
        # pass  # BAD PROGRAMMER! NO BISCUIT!
    else:
        print(result)
    finally:
        print("Beep!")


# print(dir(__builtins__))

with suppress(FileExistsError):
    os.mkdir('spam')




