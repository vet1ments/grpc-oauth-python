# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: grpcoauth/v1/oauth.proto
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
    'grpcoauth/v1/oauth.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from grpcoauth.v1 import enums_pb2 as grpcoauth_dot_v1_dot_enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18grpcoauth/v1/oauth.proto\x12\x0cgrpcoauth.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x18grpcoauth/v1/enums.proto\"}\n\x08OauthApp\x12*\n\x04role\x18\x01 \x01(\x0e\x32\x16.grpcoauth.v1.RoleTypeR\x04role\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12!\n\x0credirect_uri\x18\x04 \x01(\tR\x0bredirectUri\"\xce\x01\n\x0fGetTokenRequest\x12\x1d\n\ngrant_type\x18\x01 \x01(\tR\tgrantType\x12\x1b\n\tclient_id\x18\x02 \x01(\tR\x08\x63lientId\x12!\n\x0credirect_uri\x18\x03 \x01(\tR\x0bredirectUri\x12\x12\n\x04\x63ode\x18\x04 \x01(\tR\x04\x63ode\x12#\n\rclient_secret\x18\x05 \x01(\tR\x0c\x63lientSecret\x12#\n\rrefresh_token\x18\x06 \x01(\tR\x0crefreshToken\"\xe7\x01\n\x10GetTokenResponse\x12\x1d\n\ntoken_type\x18\x01 \x01(\tR\ttokenType\x12!\n\x0c\x61\x63\x63\x65ss_token\x18\x02 \x01(\tR\x0b\x61\x63\x63\x65ssToken\x12\x1d\n\nexpires_in\x18\x03 \x01(\x03R\texpiresIn\x12#\n\rrefresh_token\x18\x04 \x01(\tR\x0crefreshToken\x12\x37\n\x18refresh_token_expires_in\x18\x05 \x01(\x03R\x15refreshTokenExpiresIn\x12\x14\n\x05scope\x18\x06 \x03(\tR\x05scope\"\x94\x01\n\x17GetAuthorizeCodeRequest\x12\x1b\n\tclient_id\x18\x01 \x01(\tR\x08\x63lientId\x12!\n\x0credirect_uri\x18\x02 \x01(\tR\x0bredirectUri\x12#\n\rresponse_type\x18\x03 \x01(\tR\x0cresponseType\x12\x14\n\x05state\x18\x04 \x01(\tR\x05state\"D\n\x18GetAuthorizeCodeResponse\x12\x12\n\x04\x63ode\x18\x01 \x01(\tR\x04\x63ode\x12\x14\n\x05state\x18\x02 \x01(\tR\x05state\";\n\x0f\x43\x61llbackRequest\x12\x12\n\x04\x63ode\x18\x01 \x01(\tR\x04\x63ode\x12\x14\n\x05state\x18\x02 \x01(\tR\x05state2\xf0\x01\n\rOauth2Service\x12{\n\x10GetAuthorizeCode\x12%.grpcoauth.v1.GetAuthorizeCodeRequest\x1a&.grpcoauth.v1.GetAuthorizeCodeResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/oauth/authorize\x12\x62\n\x08GetToken\x12\x1d.grpcoauth.v1.GetTokenRequest\x1a\x1e.grpcoauth.v1.GetTokenResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/oauth/token:\x01*2n\n\x14OauthCallbackService\x12V\n\x08\x43\x61llback\x12\x1d.grpcoauth.v1.CallbackRequest\x1a\x16.google.protobuf.Empty\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/callback/*B\xab\x01\n\x10\x63om.grpcoauth.v1B\nOauthProtoP\x01Z:github.com/vet1ments/grpcoauth/go/grpcoauth/v1;grpcoauthv1\xa2\x02\x03GXX\xaa\x02\x0cGrpcoauth.V1\xca\x02\x0cGrpcoauth\\V1\xe2\x02\x18Grpcoauth\\V1\\GPBMetadata\xea\x02\rGrpcoauth::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpcoauth.v1.oauth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.grpcoauth.v1B\nOauthProtoP\001Z:github.com/vet1ments/grpcoauth/go/grpcoauth/v1;grpcoauthv1\242\002\003GXX\252\002\014Grpcoauth.V1\312\002\014Grpcoauth\\V1\342\002\030Grpcoauth\\V1\\GPBMetadata\352\002\rGrpcoauth::V1'
  _globals['_OAUTH2SERVICE'].methods_by_name['GetAuthorizeCode']._loaded_options = None
  _globals['_OAUTH2SERVICE'].methods_by_name['GetAuthorizeCode']._serialized_options = b'\202\323\344\223\002\022\022\020/oauth/authorize'
  _globals['_OAUTH2SERVICE'].methods_by_name['GetToken']._loaded_options = None
  _globals['_OAUTH2SERVICE'].methods_by_name['GetToken']._serialized_options = b'\202\323\344\223\002\021\"\014/oauth/token:\001*'
  _globals['_OAUTHCALLBACKSERVICE'].methods_by_name['Callback']._loaded_options = None
  _globals['_OAUTHCALLBACKSERVICE'].methods_by_name['Callback']._serialized_options = b'\202\323\344\223\002\r\022\013/callback/*'
  _globals['_OAUTHAPP']._serialized_start=127
  _globals['_OAUTHAPP']._serialized_end=252
  _globals['_GETTOKENREQUEST']._serialized_start=255
  _globals['_GETTOKENREQUEST']._serialized_end=461
  _globals['_GETTOKENRESPONSE']._serialized_start=464
  _globals['_GETTOKENRESPONSE']._serialized_end=695
  _globals['_GETAUTHORIZECODEREQUEST']._serialized_start=698
  _globals['_GETAUTHORIZECODEREQUEST']._serialized_end=846
  _globals['_GETAUTHORIZECODERESPONSE']._serialized_start=848
  _globals['_GETAUTHORIZECODERESPONSE']._serialized_end=916
  _globals['_CALLBACKREQUEST']._serialized_start=918
  _globals['_CALLBACKREQUEST']._serialized_end=977
  _globals['_OAUTH2SERVICE']._serialized_start=980
  _globals['_OAUTH2SERVICE']._serialized_end=1220
  _globals['_OAUTHCALLBACKSERVICE']._serialized_start=1222
  _globals['_OAUTHCALLBACKSERVICE']._serialized_end=1332
# @@protoc_insertion_point(module_scope)
