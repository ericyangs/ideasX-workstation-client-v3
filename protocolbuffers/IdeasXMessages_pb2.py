# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IdeasXMessages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='IdeasXMessages.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x14IdeasXMessages.proto\"\xb1\x03\n\rHealthMessage\x12\x11\n\tmodule_id\x18\x01 \x02(\x0c\x12\r\n\x05\x61live\x18\x02 \x02(\x08\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08\x12\n\n\x02lb\x18\x04 \x02(\x08\x12\x0b\n\x03ota\x18\x05 \x02(\x08\x12\x10\n\x08\x63harging\x18\x06 \x01(\x08\x12\x0b\n\x03soc\x18\x07 \x01(\x05\x12\r\n\x05vcell\x18\x08 \x02(\x05\x12\x1f\n\x03rom\x18\t \x02(\x0e\x32\x12.HealthMessage.Rom\x12\x18\n\x10\x66irmware_version\x18\n \x02(\x05\x12\x18\n\x10hardware_version\x18\x0b \x02(\x05\x12\x0c\n\x04rssi\x18\x0c \x02(\x05\x12\x0c\n\x04ssid\x18\r \x02(\t\x12\r\n\x05\x62ssid\x18\x0e \x01(\t\x12!\n\x04\x61uth\x18\x0f \x02(\x0e\x32\x13.HealthMessage.Auth\"#\n\x03Rom\x12\x08\n\x04ROM0\x10\x00\x12\x08\n\x04ROM1\x10\x01\x12\x08\n\x04ROM2\x10\x02\"_\n\x04\x41uth\x12\r\n\tAUTH_OPEN\x10\x00\x12\x0c\n\x08\x41UTH_WEP\x10\x01\x12\x10\n\x0c\x41UTH_WPA_PSK\x10\x02\x12\x11\n\rAUTH_WPA2_PSK\x10\x03\x12\x15\n\x11\x41UTH_WPA_WPA2_PSK\x10\x04\"2\n\x0b\x44\x61taMessage\x12\x0e\n\x06\x62utton\x18\x01 \x02(\x05\x12\x13\n\x0bimu_samples\x18\x02 \x01(\x0c\"\x96\x01\n\x0e\x43ommandMessage\x12(\n\x07\x63ommand\x18\x01 \x02(\x0e\x32\x17.CommandMessage.Command\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"I\n\x07\x43ommand\x12\x0e\n\nOTA_UPDATE\x10\x00\x12\r\n\tSHUT_DOWN\x10\x01\x12\x0b\n\x07UART_TX\x10\x02\x12\x12\n\x0eLSM6DS3_CONFIG\x10\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_HEALTHMESSAGE_ROM = _descriptor.EnumDescriptor(
  name='Rom',
  full_name='HealthMessage.Rom',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROM0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROM1', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROM2', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=326,
  serialized_end=361,
)
_sym_db.RegisterEnumDescriptor(_HEALTHMESSAGE_ROM)

_HEALTHMESSAGE_AUTH = _descriptor.EnumDescriptor(
  name='Auth',
  full_name='HealthMessage.Auth',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTH_OPEN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_WEP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_WPA_PSK', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_WPA2_PSK', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTH_WPA_WPA2_PSK', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=363,
  serialized_end=458,
)
_sym_db.RegisterEnumDescriptor(_HEALTHMESSAGE_AUTH)

_COMMANDMESSAGE_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='CommandMessage.Command',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OTA_UPDATE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUT_DOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UART_TX', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LSM6DS3_CONFIG', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=590,
  serialized_end=663,
)
_sym_db.RegisterEnumDescriptor(_COMMANDMESSAGE_COMMAND)


_HEALTHMESSAGE = _descriptor.Descriptor(
  name='HealthMessage',
  full_name='HealthMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='module_id', full_name='HealthMessage.module_id', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alive', full_name='HealthMessage.alive', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active', full_name='HealthMessage.active', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lb', full_name='HealthMessage.lb', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ota', full_name='HealthMessage.ota', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='charging', full_name='HealthMessage.charging', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='soc', full_name='HealthMessage.soc', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vcell', full_name='HealthMessage.vcell', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rom', full_name='HealthMessage.rom', index=8,
      number=9, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firmware_version', full_name='HealthMessage.firmware_version', index=9,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hardware_version', full_name='HealthMessage.hardware_version', index=10,
      number=11, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rssi', full_name='HealthMessage.rssi', index=11,
      number=12, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ssid', full_name='HealthMessage.ssid', index=12,
      number=13, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bssid', full_name='HealthMessage.bssid', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth', full_name='HealthMessage.auth', index=14,
      number=15, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HEALTHMESSAGE_ROM,
    _HEALTHMESSAGE_AUTH,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=458,
)


_DATAMESSAGE = _descriptor.Descriptor(
  name='DataMessage',
  full_name='DataMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='button', full_name='DataMessage.button', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='imu_samples', full_name='DataMessage.imu_samples', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=510,
)


_COMMANDMESSAGE = _descriptor.Descriptor(
  name='CommandMessage',
  full_name='CommandMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='CommandMessage.command', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='CommandMessage.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMANDMESSAGE_COMMAND,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=513,
  serialized_end=663,
)

_HEALTHMESSAGE.fields_by_name['rom'].enum_type = _HEALTHMESSAGE_ROM
_HEALTHMESSAGE.fields_by_name['auth'].enum_type = _HEALTHMESSAGE_AUTH
_HEALTHMESSAGE_ROM.containing_type = _HEALTHMESSAGE
_HEALTHMESSAGE_AUTH.containing_type = _HEALTHMESSAGE
_COMMANDMESSAGE.fields_by_name['command'].enum_type = _COMMANDMESSAGE_COMMAND
_COMMANDMESSAGE_COMMAND.containing_type = _COMMANDMESSAGE
DESCRIPTOR.message_types_by_name['HealthMessage'] = _HEALTHMESSAGE
DESCRIPTOR.message_types_by_name['DataMessage'] = _DATAMESSAGE
DESCRIPTOR.message_types_by_name['CommandMessage'] = _COMMANDMESSAGE

HealthMessage = _reflection.GeneratedProtocolMessageType('HealthMessage', (_message.Message,), dict(
  DESCRIPTOR = _HEALTHMESSAGE,
  __module__ = 'IdeasXMessages_pb2'
  # @@protoc_insertion_point(class_scope:HealthMessage)
  ))
_sym_db.RegisterMessage(HealthMessage)

DataMessage = _reflection.GeneratedProtocolMessageType('DataMessage', (_message.Message,), dict(
  DESCRIPTOR = _DATAMESSAGE,
  __module__ = 'IdeasXMessages_pb2'
  # @@protoc_insertion_point(class_scope:DataMessage)
  ))
_sym_db.RegisterMessage(DataMessage)

CommandMessage = _reflection.GeneratedProtocolMessageType('CommandMessage', (_message.Message,), dict(
  DESCRIPTOR = _COMMANDMESSAGE,
  __module__ = 'IdeasXMessages_pb2'
  # @@protoc_insertion_point(class_scope:CommandMessage)
  ))
_sym_db.RegisterMessage(CommandMessage)


# @@protoc_insertion_point(module_scope)
