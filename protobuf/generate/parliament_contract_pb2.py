# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parliament_contract.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import acs3_pb2 as acs3__pb2
try:
  aelf_dot_core__pb2 = acs3__pb2.aelf_dot_core__pb2
except AttributeError:
  aelf_dot_core__pb2 = acs3__pb2.aelf.core_pb2
try:
  google_dot_protobuf_dot_timestamp__pb2 = acs3__pb2.google_dot_protobuf_dot_timestamp__pb2
except AttributeError:
  google_dot_protobuf_dot_timestamp__pb2 = acs3__pb2.google.protobuf.timestamp_pb2
from aelf import options_pb2 as aelf_dot_options__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2

from aelf.options_pb2 import *

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19parliament_contract.proto\x12\nParliament\x1a\nacs3.proto\x1a\x12\x61\x65lf/options.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xd3\x01\n\x17\x43reateOrganizationInput\x12\x42\n\x1aproposal_release_threshold\x18\x01 \x01(\x0b\x32\x1e.acs3.ProposalReleaseThreshold\x12#\n\x1bproposer_authority_required\x18\x02 \x01(\x08\x12+\n#parliament_member_proposing_allowed\x18\x03 \x01(\x08\x12\"\n\x0e\x63reation_token\x18\x04 \x01(\x0b\x32\n.aelf.Hash\"\x9c\x02\n\x0cOrganization\x12#\n\x1bproposer_authority_required\x18\x01 \x01(\x08\x12+\n\x14organization_address\x18\x02 \x01(\x0b\x32\r.aelf.Address\x12%\n\x11organization_hash\x18\x03 \x01(\x0b\x32\n.aelf.Hash\x12\x42\n\x1aproposal_release_threshold\x18\x04 \x01(\x0b\x32\x1e.acs3.ProposalReleaseThreshold\x12+\n#parliament_member_proposing_allowed\x18\x05 \x01(\x08\x12\"\n\x0e\x63reation_token\x18\x06 \x01(\x0b\x32\n.aelf.Hash\"\x8b\x03\n\x0cProposalInfo\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x0b\x32\n.aelf.Hash\x12\x1c\n\x14\x63ontract_method_name\x18\x02 \x01(\t\x12!\n\nto_address\x18\x03 \x01(\x0b\x32\r.aelf.Address\x12\x0e\n\x06params\x18\x04 \x01(\x0c\x12\x30\n\x0c\x65xpired_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1f\n\x08proposer\x18\x06 \x01(\x0b\x32\r.aelf.Address\x12+\n\x14organization_address\x18\x07 \x01(\x0b\x32\r.aelf.Address\x12 \n\tapprovals\x18\x08 \x03(\x0b\x32\r.aelf.Address\x12!\n\nrejections\x18\t \x03(\x0b\x32\r.aelf.Address\x12\"\n\x0b\x61\x62stentions\x18\n \x03(\x0b\x32\r.aelf.Address\x12 \n\x18proposal_description_url\x18\x0b \x01(\t\"b\n\x0fInitializeInput\x12*\n\x13privileged_proposer\x18\x01 \x01(\x0b\x32\r.aelf.Address\x12#\n\x1bproposer_authority_required\x18\x02 \x01(\x08\"2\n\x0eProposalIdList\x12 \n\x0cproposal_ids\x18\x01 \x03(\x0b\x32\n.aelf.Hash\"\xa1\x01\n\'CreateOrganizationBySystemContractInput\x12H\n\x1borganization_creation_input\x18\x01 \x01(\x0b\x32#.Parliament.CreateOrganizationInput\x12,\n$organization_address_feedback_method\x18\x02 \x01(\t2\xc9\n\n\x12ParliamentContract\x12\x43\n\nInitialize\x12\x1b.Parliament.InitializeInput\x1a\x16.google.protobuf.Empty\"\x00\x12J\n\x12\x43reateOrganization\x12#.Parliament.CreateOrganizationInput\x1a\r.aelf.Address\"\x00\x12M\n\x15\x41pproveMultiProposals\x12\x1a.Parliament.ProposalIdList\x1a\x16.google.protobuf.Empty\"\x00\x12j\n\"CreateOrganizationBySystemContract\x12\x33.Parliament.CreateOrganizationBySystemContractInput\x1a\r.aelf.Address\"\x00\x12W\n#CreateEmergencyResponseOrganization\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x12\x41\n\x0fGetOrganization\x12\r.aelf.Address\x1a\x18.Parliament.Organization\"\x05\x88\x89\xf7\x01\x01\x12M\n\x1dGetDefaultOrganizationAddress\x12\x16.google.protobuf.Empty\x1a\r.aelf.Address\"\x05\x88\x89\xf7\x01\x01\x12U\n!ValidateAddressIsParliamentMember\x12\r.aelf.Address\x1a\x1a.google.protobuf.BoolValue\"\x05\x88\x89\xf7\x01\x01\x12N\n\x14GetProposerWhiteList\x12\x16.google.protobuf.Empty\x1a\x17.acs3.ProposerWhiteList\"\x05\x88\x89\xf7\x01\x01\x12\\\n\x1bGetNotVotedPendingProposals\x12\x1a.Parliament.ProposalIdList\x1a\x1a.Parliament.ProposalIdList\"\x05\x88\x89\xf7\x01\x01\x12U\n\x14GetNotVotedProposals\x12\x1a.Parliament.ProposalIdList\x1a\x1a.Parliament.ProposalIdList\"\x05\x88\x89\xf7\x01\x01\x12\x64\n#GetReleaseThresholdReachedProposals\x12\x1a.Parliament.ProposalIdList\x1a\x1a.Parliament.ProposalIdList\"\x05\x88\x89\xf7\x01\x01\x12V\n\x15GetAvailableProposals\x12\x1a.Parliament.ProposalIdList\x1a\x1a.Parliament.ProposalIdList\"\x05\x88\x89\xf7\x01\x01\x12Y\n\x1c\x43\x61lculateOrganizationAddress\x12#.Parliament.CreateOrganizationInput\x1a\r.aelf.Address\"\x05\x88\x89\xf7\x01\x01\x12W\n\'GetEmergencyResponseOrganizationAddress\x12\x16.google.protobuf.Empty\x1a\r.aelf.Address\"\x05\x88\x89\xf7\x01\x01\x1a.\xb2\xcc\xf6\x01)AElf.Contracts.Parliament.ParliamentStateB\x1c\xaa\x02\x19\x41\x45lf.Contracts.ParliamentP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'parliament_contract_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\031AElf.Contracts.Parliament'
  _PARLIAMENTCONTRACT._options = None
  _PARLIAMENTCONTRACT._serialized_options = b'\262\314\366\001)AElf.Contracts.Parliament.ParliamentState'
  _PARLIAMENTCONTRACT.methods_by_name['GetOrganization']._options = None
  _PARLIAMENTCONTRACT.methods_by_name['GetOrganization']._serialized_options = b'\210\211\367\001\001'
  _PARLIAMENTCONTRACT.methods_by_name['GetDefaultOrganizationAddress']._options = None
  _PARLIAMENTCONTRACT.methods_by_name['GetDefaultOrganizationAddress']._serialized_options = b'\210\211\367\001\001'
  _PARLIAMENTCONTRACT.methods_by_name['ValidateAddressIsParliamentMember']._options = None
  _PARLIAMENTCONTRACT.methods_by_name['ValidateAddressIsParliamentMember']._serialized_options = b'\210\211\367\001\001'
  _PARLIAMENTCONTRACT.methods_by_name['GetProposerWhiteList']._options = None
  _PARLIAMENTCONTRACT.methods_by_name['GetProposerWhiteList']._serialized_options = b'\210\211\367\001\001'
  _PARLIAMENTCONTRACT.methods_by_name['GetNotVotedPendingProposals']._options = None
  _PARLIAMENTCONTRACT.methods_by_name['GetNotVotedPendingProposals']._serialized_options = b'\210\211\367\001\001'
  _PARLIAMENTCONTRACT.methods_by_name['GetNotVotedProposals']._options = None
  _PARLIAMENTCONTRACT.methods_by_name['GetNotVotedProposals']._serialized_options = b'\210\211\367\001\001'
  _PARLIAMENTCONTRACT.methods_by_name['GetReleaseThresholdReachedProposals']._options = None
  _PARLIAMENTCONTRACT.methods_by_name['GetReleaseThresholdReachedProposals']._serialized_options = b'\210\211\367\001\001'
  _PARLIAMENTCONTRACT.methods_by_name['GetAvailableProposals']._options = None
  _PARLIAMENTCONTRACT.methods_by_name['GetAvailableProposals']._serialized_options = b'\210\211\367\001\001'
  _PARLIAMENTCONTRACT.methods_by_name['CalculateOrganizationAddress']._options = None
  _PARLIAMENTCONTRACT.methods_by_name['CalculateOrganizationAddress']._serialized_options = b'\210\211\367\001\001'
  _PARLIAMENTCONTRACT.methods_by_name['GetEmergencyResponseOrganizationAddress']._options = None
  _PARLIAMENTCONTRACT.methods_by_name['GetEmergencyResponseOrganizationAddress']._serialized_options = b'\210\211\367\001\001'
  _CREATEORGANIZATIONINPUT._serialized_start=135
  _CREATEORGANIZATIONINPUT._serialized_end=346
  _ORGANIZATION._serialized_start=349
  _ORGANIZATION._serialized_end=633
  _PROPOSALINFO._serialized_start=636
  _PROPOSALINFO._serialized_end=1031
  _INITIALIZEINPUT._serialized_start=1033
  _INITIALIZEINPUT._serialized_end=1131
  _PROPOSALIDLIST._serialized_start=1133
  _PROPOSALIDLIST._serialized_end=1183
  _CREATEORGANIZATIONBYSYSTEMCONTRACTINPUT._serialized_start=1186
  _CREATEORGANIZATIONBYSYSTEMCONTRACTINPUT._serialized_end=1347
  _PARLIAMENTCONTRACT._serialized_start=1350
  _PARLIAMENTCONTRACT._serialized_end=2703
# @@protoc_insertion_point(module_scope)
