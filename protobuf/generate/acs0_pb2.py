# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: acs0.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aelf import core_pb2 as aelf_dot_core__pb2
from aelf import options_pb2 as aelf_dot_options__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2

from aelf.core_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nacs0.proto\x12\x04\x61\x63s0\x1a\x0f\x61\x65lf/core.proto\x1a\x12\x61\x65lf/options.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xd6\x01\n\x0c\x43ontractInfo\x12\x15\n\rserial_number\x18\x01 \x01(\x03\x12\x1d\n\x06\x61uthor\x18\x02 \x01(\x0b\x32\r.aelf.Address\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\x11\x12\x1d\n\tcode_hash\x18\x04 \x01(\x0b\x32\n.aelf.Hash\x12\x1a\n\x12is_system_contract\x18\x05 \x01(\x08\x12\x0f\n\x07version\x18\x06 \x01(\x05\x12\x18\n\x10\x63ontract_version\x18\x07 \x01(\t\x12\x18\n\x10is_user_contract\x18\x08 \x01(\x08\"9\n\x17\x43ontractDeploymentInput\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\x11\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x0c\"\xfb\x02\n\x1dSystemContractDeploymentInput\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\x11\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x0c\x12\x18\n\x04name\x18\x03 \x01(\x0b\x32\n.aelf.Hash\x12i\n\x1ctransaction_method_call_list\x18\x04 \x01(\x0b\x32\x43.acs0.SystemContractDeploymentInput.SystemTransactionMethodCallList\x1a\x42\n\x1bSystemTransactionMethodCall\x12\x13\n\x0bmethod_name\x18\x01 \x01(\t\x12\x0e\n\x06params\x18\x02 \x01(\x0c\x1aq\n\x1fSystemTransactionMethodCallList\x12N\n\x05value\x18\x01 \x03(\x0b\x32?.acs0.SystemContractDeploymentInput.SystemTransactionMethodCall\"C\n\x13\x43ontractUpdateInput\x12\x1e\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\r.aelf.Address\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x0c\"\xd3\x01\n\x16\x43ontractCodeCheckInput\x12\x16\n\x0e\x63ontract_input\x18\x01 \x01(\x0c\x12\x1e\n\x16is_contract_deployment\x18\x02 \x01(\x08\x12!\n\x19\x63ode_check_release_method\x18\x03 \x01(\t\x12\x30\n\x1cproposed_contract_input_hash\x18\x04 \x01(\x0b\x32\n.aelf.Hash\x12\x10\n\x08\x63\x61tegory\x18\x05 \x01(\x11\x12\x1a\n\x12is_system_contract\x18\x06 \x01(\x08\"J\n\x10\x43ontractProposed\x12\x30\n\x1cproposed_contract_input_hash\x18\x01 \x01(\x0b\x32\n.aelf.Hash:\x04\xa0\xbb\x18\x01\"\xc9\x01\n\x10\x43ontractDeployed\x12$\n\x06\x61uthor\x18\x01 \x01(\x0b\x32\r.aelf.AddressB\x05\x88\x8f\xf5\x01\x01\x12$\n\tcode_hash\x18\x02 \x01(\x0b\x32\n.aelf.HashB\x05\x88\x8f\xf5\x01\x01\x12\x1e\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\r.aelf.Address\x12\x0f\n\x07version\x18\x04 \x01(\x05\x12\x18\n\x04Name\x18\x05 \x01(\x0b\x32\n.aelf.Hash\x12\x18\n\x10\x63ontract_version\x18\x06 \x01(\t:\x04\xa0\xbb\x18\x01\"\xa1\x01\n\x11\x43odeCheckRequired\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x0c\x12\x30\n\x1cproposed_contract_input_hash\x18\x02 \x01(\x0b\x32\n.aelf.Hash\x12\x10\n\x08\x63\x61tegory\x18\x03 \x01(\x11\x12\x1a\n\x12is_system_contract\x18\x04 \x01(\x08\x12\x18\n\x10is_user_contract\x18\x05 \x01(\x08:\x04\xa0\xbb\x18\x01\"\xab\x01\n\x0b\x43odeUpdated\x12%\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\r.aelf.AddressB\x05\x88\x8f\xf5\x01\x01\x12!\n\rold_code_hash\x18\x02 \x01(\x0b\x32\n.aelf.Hash\x12!\n\rnew_code_hash\x18\x03 \x01(\x0b\x32\n.aelf.Hash\x12\x0f\n\x07version\x18\x04 \x01(\x05\x12\x18\n\x10\x63ontract_version\x18\x05 \x01(\t:\x04\xa0\xbb\x18\x01\"\x82\x01\n\rAuthorUpdated\x12%\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\r.aelf.AddressB\x05\x88\x8f\xf5\x01\x01\x12!\n\nold_author\x18\x02 \x01(\x0b\x32\r.aelf.Address\x12!\n\nnew_author\x18\x03 \x01(\x0b\x32\r.aelf.Address:\x04\xa0\xbb\x18\x01\"s\n\"ValidateSystemContractAddressInput\x12-\n\x19system_contract_hash_name\x18\x01 \x01(\x0b\x32\n.aelf.Hash\x12\x1e\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\r.aelf.Address\"i\n\x14ReleaseContractInput\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x0b\x32\n.aelf.Hash\x12\x30\n\x1cproposed_contract_input_hash\x18\x02 \x01(\x0b\x32\n.aelf.Hash\"1\n\x14\x43ontractCodeHashList\x12\x19\n\x05value\x18\x01 \x03(\x0b\x32\n.aelf.Hash\"\x94\x01\n\x13\x43ontractCodeHashMap\x12\x33\n\x05value\x18\x01 \x03(\x0b\x32$.acs0.ContractCodeHashMap.ValueEntry\x1aH\n\nValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.acs0.ContractCodeHashList:\x02\x38\x01\"d\n\x16SetContractAuthorInput\x12\'\n\x10\x63ontract_address\x18\x01 \x01(\x0b\x32\r.aelf.Address\x12!\n\nnew_author\x18\x02 \x01(\x0b\x32\r.aelf.Address\">\n\x1d\x44\x65ployUserSmartContractOutput\x12\x1d\n\tcode_hash\x18\x01 \x01(\x0b\x32\n.aelf.Hash2\x89\x0f\n\x04\x41\x43S0\x12Q\n\x19\x44\x65ploySystemSmartContract\x12#.acs0.SystemContractDeploymentInput\x1a\r.aelf.Address\"\x00\x12\x45\n\x13\x44\x65ploySmartContract\x12\x1d.acs0.ContractDeploymentInput\x1a\r.aelf.Address\"\x00\x12\x41\n\x13UpdateSmartContract\x12\x19.acs0.ContractUpdateInput\x1a\r.aelf.Address\"\x00\x12\x41\n\x12ProposeNewContract\x12\x1d.acs0.ContractDeploymentInput\x1a\n.aelf.Hash\"\x00\x12\x46\n\x18ProposeContractCodeCheck\x12\x1c.acs0.ContractCodeCheckInput\x1a\n.aelf.Hash\"\x00\x12@\n\x15ProposeUpdateContract\x12\x19.acs0.ContractUpdateInput\x1a\n.aelf.Hash\"\x00\x12O\n\x17ReleaseApprovedContract\x12\x1a.acs0.ReleaseContractInput\x1a\x16.google.protobuf.Empty\"\x00\x12R\n\x1aReleaseCodeCheckedContract\x12\x1a.acs0.ReleaseContractInput\x1a\x16.google.protobuf.Empty\"\x00\x12_\n\x17\x44\x65ployUserSmartContract\x12\x1d.acs0.ContractDeploymentInput\x1a#.acs0.DeployUserSmartContractOutput\"\x00\x12N\n\x17UpdateUserSmartContract\x12\x19.acs0.ContractUpdateInput\x1a\x16.google.protobuf.Empty\"\x00\x12X\n ReleaseApprovedUserSmartContract\x12\x1a.acs0.ReleaseContractInput\x1a\x16.google.protobuf.Empty\"\x00\x12P\n\x1ePerformDeployUserSmartContract\x12\x1d.acs0.ContractDeploymentInput\x1a\r.aelf.Address\"\x00\x12U\n\x1ePerformUpdateUserSmartContract\x12\x19.acs0.ContractUpdateInput\x1a\x16.google.protobuf.Empty\"\x00\x12K\n\x11SetContractAuthor\x12\x1c.acs0.SetContractAuthorInput\x1a\x16.google.protobuf.Empty\"\x00\x12\x63\n\x1dValidateSystemContractAddress\x12(.acs0.ValidateSystemContractAddressInput\x1a\x16.google.protobuf.Empty\"\x00\x12X\n SetContractProposerRequiredState\x12\x1a.google.protobuf.BoolValue\x1a\x16.google.protobuf.Empty\"\x00\x12Y\n\x1b\x43urrentContractSerialNumber\x12\x16.google.protobuf.Empty\x1a\x1b.google.protobuf.Int64Value\"\x05\x88\x89\xf7\x01\x01\x12;\n\x0fGetContractInfo\x12\r.aelf.Address\x1a\x12.acs0.ContractInfo\"\x05\x88\x89\xf7\x01\x01\x12\x38\n\x11GetContractAuthor\x12\r.aelf.Address\x1a\r.aelf.Address\"\x05\x88\x89\xf7\x01\x01\x12\x33\n\x0fGetContractHash\x12\r.aelf.Address\x1a\n.aelf.Hash\"\x05\x88\x89\xf7\x01\x01\x12<\n\x18GetContractAddressByName\x12\n.aelf.Hash\x1a\r.aelf.Address\"\x05\x88\x89\xf7\x01\x01\x12^\n%GetSmartContractRegistrationByAddress\x12\r.aelf.Address\x1a\x1f.aelf.SmartContractRegistration\"\x05\x88\x89\xf7\x01\x01\x12\\\n&GetSmartContractRegistrationByCodeHash\x12\n.aelf.Hash\x1a\x1f.aelf.SmartContractRegistration\"\x05\x88\x89\xf7\x01\x01\x12o\n-GetContractCodeHashListByDeployingBlockHeight\x12\x1b.google.protobuf.Int64Value\x1a\x1a.acs0.ContractCodeHashList\"\x05\x88\x89\xf7\x01\x01\x42\x16\xaa\x02\x13\x41\x45lf.Standards.ACS0P\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'acs0_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\023AElf.Standards.ACS0'
  _CONTRACTPROPOSED._options = None
  _CONTRACTPROPOSED._serialized_options = b'\240\273\030\001'
  _CONTRACTDEPLOYED.fields_by_name['author']._options = None
  _CONTRACTDEPLOYED.fields_by_name['author']._serialized_options = b'\210\217\365\001\001'
  _CONTRACTDEPLOYED.fields_by_name['code_hash']._options = None
  _CONTRACTDEPLOYED.fields_by_name['code_hash']._serialized_options = b'\210\217\365\001\001'
  _CONTRACTDEPLOYED._options = None
  _CONTRACTDEPLOYED._serialized_options = b'\240\273\030\001'
  _CODECHECKREQUIRED._options = None
  _CODECHECKREQUIRED._serialized_options = b'\240\273\030\001'
  _CODEUPDATED.fields_by_name['address']._options = None
  _CODEUPDATED.fields_by_name['address']._serialized_options = b'\210\217\365\001\001'
  _CODEUPDATED._options = None
  _CODEUPDATED._serialized_options = b'\240\273\030\001'
  _AUTHORUPDATED.fields_by_name['address']._options = None
  _AUTHORUPDATED.fields_by_name['address']._serialized_options = b'\210\217\365\001\001'
  _AUTHORUPDATED._options = None
  _AUTHORUPDATED._serialized_options = b'\240\273\030\001'
  _CONTRACTCODEHASHMAP_VALUEENTRY._options = None
  _CONTRACTCODEHASHMAP_VALUEENTRY._serialized_options = b'8\001'
  _ACS0.methods_by_name['CurrentContractSerialNumber']._options = None
  _ACS0.methods_by_name['CurrentContractSerialNumber']._serialized_options = b'\210\211\367\001\001'
  _ACS0.methods_by_name['GetContractInfo']._options = None
  _ACS0.methods_by_name['GetContractInfo']._serialized_options = b'\210\211\367\001\001'
  _ACS0.methods_by_name['GetContractAuthor']._options = None
  _ACS0.methods_by_name['GetContractAuthor']._serialized_options = b'\210\211\367\001\001'
  _ACS0.methods_by_name['GetContractHash']._options = None
  _ACS0.methods_by_name['GetContractHash']._serialized_options = b'\210\211\367\001\001'
  _ACS0.methods_by_name['GetContractAddressByName']._options = None
  _ACS0.methods_by_name['GetContractAddressByName']._serialized_options = b'\210\211\367\001\001'
  _ACS0.methods_by_name['GetSmartContractRegistrationByAddress']._options = None
  _ACS0.methods_by_name['GetSmartContractRegistrationByAddress']._serialized_options = b'\210\211\367\001\001'
  _ACS0.methods_by_name['GetSmartContractRegistrationByCodeHash']._options = None
  _ACS0.methods_by_name['GetSmartContractRegistrationByCodeHash']._serialized_options = b'\210\211\367\001\001'
  _ACS0.methods_by_name['GetContractCodeHashListByDeployingBlockHeight']._options = None
  _ACS0.methods_by_name['GetContractCodeHashListByDeployingBlockHeight']._serialized_options = b'\210\211\367\001\001'
  _CONTRACTINFO._serialized_start=119
  _CONTRACTINFO._serialized_end=333
  _CONTRACTDEPLOYMENTINPUT._serialized_start=335
  _CONTRACTDEPLOYMENTINPUT._serialized_end=392
  _SYSTEMCONTRACTDEPLOYMENTINPUT._serialized_start=395
  _SYSTEMCONTRACTDEPLOYMENTINPUT._serialized_end=774
  _SYSTEMCONTRACTDEPLOYMENTINPUT_SYSTEMTRANSACTIONMETHODCALL._serialized_start=593
  _SYSTEMCONTRACTDEPLOYMENTINPUT_SYSTEMTRANSACTIONMETHODCALL._serialized_end=659
  _SYSTEMCONTRACTDEPLOYMENTINPUT_SYSTEMTRANSACTIONMETHODCALLLIST._serialized_start=661
  _SYSTEMCONTRACTDEPLOYMENTINPUT_SYSTEMTRANSACTIONMETHODCALLLIST._serialized_end=774
  _CONTRACTUPDATEINPUT._serialized_start=776
  _CONTRACTUPDATEINPUT._serialized_end=843
  _CONTRACTCODECHECKINPUT._serialized_start=846
  _CONTRACTCODECHECKINPUT._serialized_end=1057
  _CONTRACTPROPOSED._serialized_start=1059
  _CONTRACTPROPOSED._serialized_end=1133
  _CONTRACTDEPLOYED._serialized_start=1136
  _CONTRACTDEPLOYED._serialized_end=1337
  _CODECHECKREQUIRED._serialized_start=1340
  _CODECHECKREQUIRED._serialized_end=1501
  _CODEUPDATED._serialized_start=1504
  _CODEUPDATED._serialized_end=1675
  _AUTHORUPDATED._serialized_start=1678
  _AUTHORUPDATED._serialized_end=1808
  _VALIDATESYSTEMCONTRACTADDRESSINPUT._serialized_start=1810
  _VALIDATESYSTEMCONTRACTADDRESSINPUT._serialized_end=1925
  _RELEASECONTRACTINPUT._serialized_start=1927
  _RELEASECONTRACTINPUT._serialized_end=2032
  _CONTRACTCODEHASHLIST._serialized_start=2034
  _CONTRACTCODEHASHLIST._serialized_end=2083
  _CONTRACTCODEHASHMAP._serialized_start=2086
  _CONTRACTCODEHASHMAP._serialized_end=2234
  _CONTRACTCODEHASHMAP_VALUEENTRY._serialized_start=2162
  _CONTRACTCODEHASHMAP_VALUEENTRY._serialized_end=2234
  _SETCONTRACTAUTHORINPUT._serialized_start=2236
  _SETCONTRACTAUTHORINPUT._serialized_end=2336
  _DEPLOYUSERSMARTCONTRACTOUTPUT._serialized_start=2338
  _DEPLOYUSERSMARTCONTRACTOUTPUT._serialized_end=2400
  _ACS0._serialized_start=2403
  _ACS0._serialized_end=4332
# @@protoc_insertion_point(module_scope)
