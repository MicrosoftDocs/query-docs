---
title: "Binary functions | Microsoft Docs"
ms.date: 4/7/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Binary functions

These functions convert and manipulate binary data.
  
## <a name="__toc362450785"></a>Binary Formats  
  
### <a name="__toc356573186"></a>Reading numbers  
  
|Function|Description|  
|------------|---------------|  
|[BinaryFormat.7BitEncodedSignedInteger](binaryformat-7bitencodedsignedinteger.md)|A binary format that reads a 64-bit signed integer that was encoded using a 7-bit variable-length encoding.|  
|[BinaryFormat.7BitEncodedUnsignedInteger](binaryformat-7bitencodedunsignedinteger.md)|A binary format that reads a 64-bit unsigned integer that was encoded using a 7-bit variable-length encoding.|  
|[BinaryFormat.Binary](binaryformat-binary.md)|Returns a binary format that reads a binary value.|  
|[BinaryFormat.Byte](binaryformat-byte.md)|A binary format that reads an 8-bit unsigned integer.|  
|[BinaryFormat.Choice](binaryformat-choice.md)|Returns a binary format that chooses the next binary format based on a value that has already been read.|  
|[BinaryFormat.Decimal](binaryformat-decimal.md)|A binary format that reads a .NET 16-byte decimal value.| 
|[BinaryFormat.Double](binaryformat-double.md)|A binary format that reads an 8-byte IEEE double-precision floating point value.|  
|[BinaryFormat.Group](binaryformat-group.md)|Returns a binary format that reads a group of items. Each item value is preceded by a unique key value. The result is a list of item values.|  
|[BinaryFormat.Length](binaryformat-length.md)|Returns a binary format that limits the amount of data that can be read. Both BinaryFormat.List and BinaryFormat.Binary can be used to read until end of the data. BinaryFormat.Length can be used to limit the number of bytes that are read.|  
|[BinaryFormat.List](binaryformat-list.md)|Returns a binary format that reads a sequence of items and returns a list.|  
|[BinaryFormat.Null](binaryformat-null.md)|A binary format that reads zero bytes and returns null.|  
|[BinaryFormat.Record](binaryformat-record.md)|Returns a binary format that reads a record. Each field in the record can have a different binary format.|  
|[BinaryFormat.SignedInteger16](binaryformat-signedinteger16.md)|A binary format that reads a 16-bit signed integer.|
|[BinaryFormat.SignedInteger32](binaryformat-signedinteger32.md)|A binary format that reads a 32-bit signed integer.|  
|[BinaryFormat.SignedInteger64](binaryformat-signedinteger64.md)|A binary format that reads a 64-bit signed integer.|  
|[BinaryFormat.Single](binaryformat-single.md)|A binary format that reads a 4-byte IEEE single-precision floating point value.|  
|[BinaryFormat.Text](binaryformat-text.md)|Returns a binary format that reads a text value. The optional encoding value specifies the encoding of the text.|  
|[BinaryFormat.Transform](binaryformat-transform.md)|Returns a binary format that will transform the values read by another binary format.|  
|[BinaryFormat.UnsignedInteger16](binaryformat-unsignedinteger16.md)|A binary format that reads a 16-bit unsigned integer.|  
|[BinaryFormat.UnsignedInteger32](binaryformat-unsignedinteger32.md)|A binary format that reads a 32-bit unsigned integer.|  
|[BinaryFormat.UnsignedInteger64](binaryformat-unsignedinteger64.md)|A binary format that reads a 64-bit unsigned integer.|  

Controlling byte order | Description
---------------------- | -----------
[BinaryFormat.ByteOrder](binaryformat-byteorder.md) | Returns a binary format with the byte order specified by a function.
[Table.PartitionValues](table-partitionvalues.md) | Returns information about how a table is partitioned.
  
## <a name="__toc362450796"></a>Binary  
  
|Function|Description|  
|------------|---------------|  
|[Binary.Buffer](binary-buffer.md)|Buffers the binary value in memory. The result of this call is a stable binary value, which means it will have a deterministic length and order of bytes.|  
|[Binary.Combine](binary-combine.md)|Combines a list of binaries into a single binary.|
|[Binary.Compress](binary-compress.md)|Compresses a binary value using the given compression type.|
|[Binary.Decompress](binary-decompress.md)|Decompresses a binary value using the given compression type.|  
|[Binary.From](binary-from.md)|Returns a binary value from the given value.|  
|[Binary.FromList](binary-fromlist.md)|Converts a list of numbers into a binary value|  
|[Binary.FromText](binary-fromtext.md)|Decodes data from a text form into binary.|  
|[Binary.InferContentType](binary-infercontenttype.md)|Returns a record with field Content.Type that contains the inferred MIME-type.|  
|[Binary.Length](binary-length.md)|Returns the length of binary values.|  
|[Binary.ToList](binary-tolist.md)|Converts a binary value into a list of numbers|  
|[Binary.ToText](binary-totext.md)|Encodes binary data into a text form.|  
|[BinaryEncoding.Base64](binaryencoding-base64.md)|Constant to use as the encoding type when base-64 encoding is required.|
|[BinaryEncoding.Hex](binaryencoding-hex.md)|Constant to use as the encoding type when hexadecimal encoding is required.|
|[BinaryOccurrence.Optional](binaryoccurrence-optional.md)|The item is expected to appear zero or one time in the input.|
|[BinaryOccurrence.Repeating](binaryoccurrence-repeating.md)|The item is expected to appear zero or more times in the input.|
|[BinaryOccurrence.Required](binaryoccurrence-required.md)|The item is expected to appear once in the input.|
|[ByteOrder.BigEndian](byteorder-bigendian.md)|A possible value for the `byteOrder` parameter in `BinaryFormat.ByteOrder`. The most signficant byte appears first in Big Endian byte order.|
|[ByteOrder.LittleEndian](byteorder-littleendian.md)|A possible value for the `byteOrder` parameter in `BinaryFormat.ByteOrder`. The least signficant byte appears first in Little Endian byte order.|
|[Compression.Deflate](compression-deflate.md)|The compressed data is in the 'Deflate' format.|
|[Compression.GZip](compression-gzip.md)|The compressed data is in the 'GZip' format.|
|[Occurrence.Optional](occurrence-optional.md) | The item is expected to appear zero or one time in the input.|
|[Occurrence.Repeating](occurrence-repeating.md) | The item is expected to appear zero or more times in the input.|
|[Occurrence.Required](occurrence-required.md) | The item is expected to appear once in the input.|
|[#binary](sharpbinary.md) | Creates a binary value from numbers or text.|

