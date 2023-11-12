import json
import base58
import base64
from aelf.client import AElf
from aelf.toolkits import AElfToolkit
from aelf.types_pb2 import Transaction, Hash, Address, TransactionFeeCharged, ResourceTokenCharged
from coincurve import PrivateKey
from google.protobuf.json_format import MessageToJson
from protobuf.generate import token_contract_pb2 as TokenContract


class AElfClient():
    _client = None

    def __init__(self, _url):
        self._client = AElf(_url,"aelf","aelf")


    def create_transaction(self, to_address, method_name, params=None):
        """
        Create transaction
        :param to_address: to address
        :param method_name: method name
        :param params: params for method
        :return: transaction object
        """
        chain_status = self._client.get_chain_status()
        best_chain_hash = chain_status['BestChainHash']
        best_chain_height = chain_status['BestChainHeight']

        if not isinstance(to_address, Address):
            to_address_string = to_address
            to_address = Address()
            to_address.value = base58.b58decode_check(to_address_string)

        transaction = Transaction()
        transaction.to_address.CopyFrom(to_address)
        transaction.method_name = method_name
        if params is not None:
            transaction.params = params
        transaction.ref_block_number = best_chain_height
        transaction.ref_block_prefix = bytes(bytearray.fromhex(best_chain_hash)[:4])
        return transaction

    def call(self, private_key_string, to_address, method_name, protobuf_result, params=None):
        """
        Create transaction and call
        """
        private_key = PrivateKey(bytes(bytearray.fromhex(private_key_string)))

        paramVal = params
        if params is not None:
            paramVal = params.SerializeToString()
        tx = self.create_transaction(to_address, method_name, paramVal)
        tx = self._client.sign_transaction(private_key, tx)
#         print('>>> sign tx', tx.signature)

        out = self._client.execute_transaction(tx.SerializePartialToString().hex())
        out_hex_str = out.decode('ascii')
#         print('>>> call res', out_hex_str)
        protobuf_result.ParseFromString(bytes.fromhex(out_hex_str))
        return protobuf_result

    def send(self, private_key_string, to_address, method_name, params=None):
        """
        Create transaction and call
        """
        private_key = PrivateKey(bytes(bytearray.fromhex(private_key_string)))

        paramVal = params
        if params is not None:
            paramVal = params.SerializeToString()
        tx = self.create_transaction(to_address, method_name, paramVal)
        tx = self._client.sign_transaction(private_key, tx)
        # print('>>> sign tx', tx.signature)
        result = self._client.send_transaction(tx.SerializePartialToString().hex())
        return result

    def get_transaction_result(self, transaction_id):
        return self._client.get_transaction_result(transaction_id)

    @staticmethod
    def object_to_json(obj, format=False):
        """
        Convert an object to a JSON string.
        If the object is a string, return it as is.
        If it's a Protobuf object, convert it to a JSON string.
        Otherwise, try to convert it to a JSON string using json.dumps.

        :param obj: The object to convert.
        :param format: Boolean, whether to format the JSON output. Default is False.
        :return: A JSON string representation of the object.
        """
        if isinstance(obj, str):
            return obj
        elif hasattr(obj, 'DESCRIPTOR'):
            json_string = MessageToJson(obj)
            if format:
                return json.dumps(json.loads(json_string), indent=4)
            return json_string
        else:
            try:
                return json.dumps(obj, indent=4 if format else None)
            except TypeError:
                return "Object cannot be converted to JSON"