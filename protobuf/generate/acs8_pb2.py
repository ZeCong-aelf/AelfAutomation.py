# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: acs8.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from aelf import options_pb2 as aelf_dot_options__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2

from aelf.options_pb2 import *
from google.protobuf.empty_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nacs8.proto\x12\x04\x61\x63s8\x1a\x12\x61\x65lf/options.proto\x1a\x1bgoogle/protobuf/empty.proto\"J\n\x15\x42uyResourceTokenInput\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\x11\n\tpay_limit\x18\x03 \x01(\x03\x32h\n\x1bResourceConsumptionContract\x12I\n\x10\x42uyResourceToken\x12\x1b.acs8.BuyResourceTokenInput\x1a\x16.google.protobuf.Empty\"\x00\x42\x1f\xaa\x02\x13\x41\x45lf.Standards.ACS8\x8a\x92\xf4\x01\x04\x61\x63s8P\x00P\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'acs8_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\023AElf.Standards.ACS8\212\222\364\001\004acs8'
  _BUYRESOURCETOKENINPUT._serialized_start=69
  _BUYRESOURCETOKENINPUT._serialized_end=143
  _RESOURCECONSUMPTIONCONTRACT._serialized_start=145
  _RESOURCECONSUMPTIONCONTRACT._serialized_end=249
# @@protoc_insertion_point(module_scope)