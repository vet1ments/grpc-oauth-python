# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: oauthapp/v1/token.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'oauthapp/v1/token.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17oauthapp/v1/token.proto\x12\x0boauthapp.v1\"\'\n\x0fGetTokenRequest\x12\x14\n\x05state\x18\x01 \x01(\tR\x05state\"\xb2\x01\n\x10GetTokenResponse\x12!\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\tR\x0b\x61\x63\x63\x65ssToken\x12\x1d\n\nexpires_in\x18\x02 \x01(\x03R\texpiresIn\x12#\n\rrefresh_token\x18\x03 \x01(\tR\x0crefreshToken\x12\x37\n\x18refresh_token_expires_in\x18\x04 \x01(\x03R\x15refreshTokenExpiresIn\"+\n\x13GetTokenInfoRequest\x12\x14\n\x05token\x18\x01 \x01(\tR\x05token\",\n\x14GetTokenInfoResponse\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token2\xab\x01\n\x0bTokeService\x12G\n\x08GetToken\x12\x1c.oauthapp.v1.GetTokenRequest\x1a\x1d.oauthapp.v1.GetTokenResponse\x12S\n\x0cGetTokenInfo\x12 .oauthapp.v1.GetTokenInfoRequest\x1a!.oauthapp.v1.GetTokenInfoResponseB\xa4\x01\n\x0f\x63om.oauthapp.v1B\nTokenProtoP\x01Z8github.com/vet1ments/grpcoauth/go/oauthapp/v1;oauthappv1\xa2\x02\x03OXX\xaa\x02\x0bOauthapp.V1\xca\x02\x0bOauthapp\\V1\xe2\x02\x17Oauthapp\\V1\\GPBMetadata\xea\x02\x0cOauthapp::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'oauthapp.v1.token_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.oauthapp.v1B\nTokenProtoP\001Z8github.com/vet1ments/grpcoauth/go/oauthapp/v1;oauthappv1\242\002\003OXX\252\002\013Oauthapp.V1\312\002\013Oauthapp\\V1\342\002\027Oauthapp\\V1\\GPBMetadata\352\002\014Oauthapp::V1'
  _globals['_GETTOKENREQUEST']._serialized_start=40
  _globals['_GETTOKENREQUEST']._serialized_end=79
  _globals['_GETTOKENRESPONSE']._serialized_start=82
  _globals['_GETTOKENRESPONSE']._serialized_end=260
  _globals['_GETTOKENINFOREQUEST']._serialized_start=262
  _globals['_GETTOKENINFOREQUEST']._serialized_end=305
  _globals['_GETTOKENINFORESPONSE']._serialized_start=307
  _globals['_GETTOKENINFORESPONSE']._serialized_end=351
  _globals['_TOKESERVICE']._serialized_start=354
  _globals['_TOKESERVICE']._serialized_end=525
# @@protoc_insertion_point(module_scope)
