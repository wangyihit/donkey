#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from thrift.protocol.TBinaryProtocol import TBinaryProtocol, TBinaryProtocolFactory
from thrift.protocol.TJSONProtocol import TJSONProtocol, TJSONProtocolFactory
from thrift.transport.TTransport import TMemoryBuffer


class ThriftSerializer(object):

    @staticmethod
    def to_binary(thrift_obj):
        memory_buffer = TMemoryBuffer()
        binary_protocol = TBinaryProtocol(memory_buffer)
        thrift_obj.write(binary_protocol)
        return memory_buffer.getvalue()

    @staticmethod
    def from_binary(thrift_obj, buf):
        transport = TMemoryBuffer(buf)
        protocol = TBinaryProtocolFactory().getProtocol(transport)
        thrift_obj.read(protocol)
        return thrift_obj

    @staticmethod
    def from_json(thrift_obj, buf):
        transport = TMemoryBuffer(buf)
        protocol = TJSONProtocolFactory().getProtocol(transport)
        thrift_obj.read(protocol)
        return thrift_obj

    @staticmethod
    def to_json(thrift_obj):
        memory_buffer = TMemoryBuffer()
        binary_protocol = TJSONProtocol(memory_buffer)
        thrift_obj.write(binary_protocol)
        return memory_buffer.getvalue()
