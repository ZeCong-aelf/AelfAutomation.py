# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aelf/options.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61\x65lf/options.proto\x12\x04\x61\x65lf\x1a google/protobuf/descriptor.proto:0\n\x08identity\x12\x1c.google.protobuf.FileOptions\x18\xa1\xc2\x1e \x01(\t:/\n\x04\x62\x61se\x12\x1f.google.protobuf.ServiceOptions\x18\xa9\xe9\x1e \x03(\t:7\n\x0c\x63sharp_state\x12\x1f.google.protobuf.ServiceOptions\x18\xc6\xe9\x1e \x01(\t:1\n\x07is_view\x12\x1e.google.protobuf.MethodOptions\x18\x91\xf1\x1e \x01(\x08:3\n\x08is_event\x12\x1f.google.protobuf.MessageOptions\x18\xb4\x87\x03 \x01(\x08:3\n\nis_indexed\x12\x1d.google.protobuf.FieldOptions\x18\xf1\xd1\x1e \x01(\x08\x42\x07\xaa\x02\x04\x41\x45lfb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aelf.options_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(identity)
  google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(base)
  google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(csharp_state)
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(is_view)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(is_event)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(is_indexed)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\004AElf'
# @@protoc_insertion_point(module_scope)
