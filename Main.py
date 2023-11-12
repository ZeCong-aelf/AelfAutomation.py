import os
import sys
import json
import base58
import base64
from symbolregistrar.SymbolRegistrar import SymbolRegistrar

_url ="http://192.168.66.3:8000"
_symbol_registrar_contract_address = "2VTusxv6BN4SQDroitnWyLyQHWiwEhdWU76PPiGBqt5VbyF27J"

_privateKey = "123301ea59b724df4d923de8f4808dea3bb0343835ff9d00d81f762318c534ce"

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python Symbol.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "SpecialSeed.add":
        if len(sys.argv) < 2:
            print("Usage: python Symbol.py AddSpecialSeed <seed_type> [<resend_pages>]")
            sys.exit(1)
        seed_type = sys.argv[2] if len(sys.argv) > 2 else None
        resend_pages = sys.argv[3] if len(sys.argv) > 3 else None
        SymbolRegistrar(_url, _symbol_registrar_contract_address, _privateKey).do_add(seed_type, resend_pages)
    elif command == "SpecialSeed.check":
        if len(sys.argv) != 3:
            print("Usage: python Symbol.py Check <result_file>")
            sys.exit(1)
        SymbolRegistrar(_url, _symbol_registrar_contract_address, _privateKey).do_check(sys.argv[2])
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)