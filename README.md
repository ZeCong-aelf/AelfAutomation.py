# AelfAutomation.py


# Files infomation

```shell
AelfAutomation.py
  |- [aelf]     // code from https://github.com/AElfProject/aelf-sdk.py 
  |- [protobuf] // AElf contract protobuf file
  |- [symbolregistrar] // symbolregistrar automation logic lode
  |- Main.py      // start up entrance
  |- notable.txt  // notable special seed list notable.txt, one line one symbol
  |- uniq.txt     // uniq special seed list notable.txt, one line one symbol
  |- notable_result_xxxxx // notable add result file
  |- uniq_result_xxxxxxxx // uniq add result file
```

Setup `_url`,`_symbol_registrar_contract_address`,`_privateKey` in `Main.py`

# actions
- `"SpecialSeed.add"`: Read txt file, Send transaction to node, Record a result file, Resend filed pages
- `"SpecialSeed.check"`: Read result file, Query transaction result and print transaction result


# Usage - Add special seed

Run Main.py file with args

- `args[0]`: command: `"SpecialSeed.add"`
- `args[1]`: type of SpecialSeed `"uniq"` or `"notable"`
- `args[2]`: `[optional]` pages of data to **RESEND**, values joined with `"," `

```shell
python3 Main.py SpecialSeed.add uniq 2,4,5
```

output file name will like this:

`notable_result_2023_11_11_16_10_10`

`notable_result_2023_11_11_16_10_10`

output file content will like this:
```shell
# page, fromSymbol, toSymbol, transactionHash
2,ARO,FEO,90589bec79316e9d58aae131645eca4de9e12e301679e3cc5912c6c99e59f386
4,JET,MEL,aa03cb99e57d7fa293e3542e9fbe3cb305d6a3968be4d5d4678e95fd08f2d47a
5,MEO,REB,77d4fa0c0c2a21c762c6f02cfef098f54b312c256c08e1c73a03e60b5d461b71
```


# Usage - Check special seed
Run Main.py file with args:
- `args[0]`: command: "SpecialSeed.check"
- `args[1]`: result fileName

```shell
python3 Main.py SpecialSeed.check uniq_result_2023_11_11_16_10_10
```

console output result will like this:

```shell
# page, fromSymbol, toSymbol, transactionHash, status, error-info
2,ARO,FEO,90589bec79316e9d58aae131645eca4de9e12e301679e3cc5912c6c99e59f386 status=NOTEXISTED, error=
4,JET,MEL,aa03cb99e57d7fa293e3542e9fbe3cb305d6a3968be4d5d4678e95fd08f2d47a status=NOTEXISTED, error=
5,MEO,REB,77d4fa0c0c2a21c762c6f02cfef098f54b312c256c08e1c73a03e60b5d461b71 status=MINED, error=
Pending pages: 
Failed pages: 2,4
```
