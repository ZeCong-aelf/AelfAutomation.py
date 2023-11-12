import os
import sys
import json
import re
import base58
import base64

from datetime import datetime
from aelf.types_pb2 import Transaction, Hash, Address, TransactionFeeCharged, ResourceTokenCharged
from aelf.AElfClient import AElfClient
from .dtos.AddResult import AddResult
from protobuf.generate import symbol_registrar_contract_pb2 as SymbolRegistrarContract

# from protobuf.generate import token_contract_pb2 as TokenContract


page_size = 50

_uniq_file = "uniq.txt"
_uniq_result_file = "uniq_result_"

_notable_file = "notable.txt"
_notable_result_file = "notable_result_"


class SymbolRegistrar:
    def __init__(self, node_url, contract_address, private_key):
        self.private_key = private_key

        self.client = AElfClient(node_url)
        self.contract_address = contract_address

        self.uniq_file = _uniq_file
        self.uniq_log_file = _uniq_result_file

        self.notable_file = _notable_file
        self.notable_log_file = _notable_result_file

    def do_add(self, type, page_string):
        page = [int(p) for p in page_string.split(",")] if page_string else []
        assert all(p > 0 for p in page), "Invalid page"

        file_path = self.uniq_file if type == "uniq" else self.notable_file
        with open(file_path, 'r') as file:
            all_lines = file.readlines()
        total_page = (len(all_lines) + page_size - 1) // page_size
        result_lines = []

        for current_page in range(1, total_page + 1):
            if page and current_page not in page:
                continue
            page_lines = all_lines[(current_page - 1) * page_size: current_page * page_size]
            page_lines = self.duplicate_list([re.sub(r'\s+', '', line).upper() for line in page_lines])
            if not page_lines:
                continue
            res = None
            if type == "uniq":
                res = self.process_page_uniq(page_lines, current_page)
            else:
                res = self.process_page_notable(page_lines, current_page)

            result_lines.append(res.to_result_line())
            result_lines.append("\n")

        result_file_path = self.uniq_log_file if type == "uniq" else self.notable_log_file
        result_file_path += datetime.utcnow().strftime('%Y_%m_%d_%H_%M_%S')
        with open(result_file_path, 'w') as file:
            file.writelines(result_lines)

    def process_page_notable(self, page_lines, current_page):
        list = SymbolRegistrarContract.SpecialSeedList()

        for symbol in page_lines:
            seed = SymbolRegistrarContract.SpecialSeed()
            seed.seed_type = SymbolRegistrarContract.SeedType.NOTABLE
            seed.auction_type = SymbolRegistrarContract.AuctionType.ENGLISH
            seed.symbol = symbol
            seed.price_amount = 1000_0000_0000
            seed.price_symbol = "ELF"
            seed.issue_chain = "ETH"
            seed.issue_chain_contract_address = "0x00"
            list.value.append(seed)

        res = self.client.send(self.private_key, self.contract_address, "AddSpecialSeeds", list)
        print(">> send result", AElfClient.object_to_json(res))

        result = AddResult(current_page, page_lines[0], page_lines[-1], res["TransactionId"])
        return result

    def process_page_uniq(self, page_lines, current_page):
        list = SymbolRegistrarContract.UniqueSeedList()
        list.symbols.extend(page_lines)

        res = self.client.send(self.private_key, self.contract_address, "AddUniqueSeeds", list)
        print(">> send result", AElfClient.object_to_json(res))

        result = AddResult(current_page, page_lines[0], page_lines[-1], res["TransactionId"])
        return result

    def do_check(self, result_file):
        result_file_path = os.path.abspath(result_file)
        with open(result_file_path, 'r') as file:
            all_lines = file.readlines()
        result_list = [AddResult.from_result_line(line.strip()) for line in all_lines]

        # 查询交易结果并打印
        pending_pages = []
        fail_pages = []
        for result_item in result_list:
            query_result = self.client.get_transaction_result(result_item.transaction_id)
            # print(">> send result", AElfClient.object_to_json(query_result))
            print(f"{result_item.to_result_line()} status={query_result['Status']}, error={query_result['Error']}")
            if query_result['Status'] == "PENDING":
                pending_pages.append(result_item.page)
            elif query_result['Status'] != "MINED":
                fail_pages.append(result_item.page)

        print("Pending pages: " + ",".join(map(str, pending_pages)))
        print("Failed pages: " + ",".join(map(str, fail_pages)))

    def duplicate_list(self, list):
        seen = set()
        result_lines_no_duplicates = []
        for line in list:
            if line not in seen:
                result_lines_no_duplicates.append(line)
                seen.add(line)
        return result_lines_no_duplicates
