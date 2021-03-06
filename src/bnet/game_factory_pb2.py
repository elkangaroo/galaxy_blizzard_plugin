# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/game_factory.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import bnet.attribute_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/game_factory.proto',
  package='bnet.protocol.game_master',
  serialized_pb=_b('\n\x17\x62net/game_factory.proto\x12\x19\x62net.protocol.game_master\x1a\x14\x62net/attribute.proto\"\xca\x01\n\x0eGameProperties\x12?\n\x13\x63reation_attributes\x18\x01 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x38\n\x06\x66ilter\x18\x02 \x01(\x0b\x32(.bnet.protocol.attribute.AttributeFilter\x12\x15\n\x06\x63reate\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x12\n\x04open\x18\x04 \x01(\x08:\x04true\x12\x12\n\nprogram_id\x18\x05 \x01(\x07')
  ,
  dependencies=[bnet.attribute_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GAMEPROPERTIES = _descriptor.Descriptor(
  name='GameProperties',
  full_name='bnet.protocol.game_master.GameProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creation_attributes', full_name='bnet.protocol.game_master.GameProperties.creation_attributes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter', full_name='bnet.protocol.game_master.GameProperties.filter', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='create', full_name='bnet.protocol.game_master.GameProperties.create', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open', full_name='bnet.protocol.game_master.GameProperties.open', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='program_id', full_name='bnet.protocol.game_master.GameProperties.program_id', index=4,
      number=5, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=279,
)

_GAMEPROPERTIES.fields_by_name['creation_attributes'].message_type = bnet.attribute_pb2._ATTRIBUTE
_GAMEPROPERTIES.fields_by_name['filter'].message_type = bnet.attribute_pb2._ATTRIBUTEFILTER
DESCRIPTOR.message_types_by_name['GameProperties'] = _GAMEPROPERTIES

GameProperties = _reflection.GeneratedProtocolMessageType('GameProperties', (_message.Message,), dict(
  DESCRIPTOR = _GAMEPROPERTIES,
  __module__ = 'bnet.game_factory_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_master.GameProperties)
  ))
_sym_db.RegisterMessage(GameProperties)


# @@protoc_insertion_point(module_scope)
