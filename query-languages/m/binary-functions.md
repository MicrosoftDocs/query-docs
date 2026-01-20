---
description: "Learn more about: Binary functions"
title: "Binary functions"
ms.date: 2/17/2023
ms.topic: language-reference
ms.custom: "nonautomated-date"
---
# Binary functions

These functions create and manipulate binary data.

## Binary Formats

### Reading numbers

|Name|Description|
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

### Controlling byte order

|Name | Description
|---------------------- | -----------|
|[BinaryFormat.ByteOrder](binaryformat-byteorder.md) | Returns a binary format with the byte order specified by a function.|
|[Table.PartitionValues](table-partitionvalues.md) | Returns information about how a table is partitioned.|

## Binary data

|Name|Description|
|------------|---------------|
|[Binary.ApproximateLength](binary-approximatelength.md)|Returns the approximate length of the binary.|
|[Binary.Buffer](binary-buffer.md)|Buffers the binary value in memory. The result of this call is a stable binary value, which means it will have a deterministic length and order of bytes.|
|[Binary.Combine](binary-combine.md)|Combines a list of binaries into a single binary.|
|[Binary.Compress](binary-compress.md)|Compresses a binary value using the given compression type.|
|[Binary.Decompress](binary-decompress.md)|Decompresses a binary value using the given compression type.|
|[Binary.From](binary-from.md)|Returns a binary value from the given value.|
|[Binary.FromList](binary-fromlist.md)|Converts a list of numbers into a binary value|
|[Binary.FromText](binary-fromtext.md)|Decodes data from a text form into binary.|
|[Binary.InferContentType](binary-infercontenttype.md)|Returns a record with field Content.Type that contains the inferred MIME-type.|
|[Binary.Length](binary-length.md)|Returns the length of binary values.|
|[Binary.Range](binary-range.md)|Returns a subset of the binary value beginning at an offset.|
|[Binary.Split](binary-split.md)|Splits the specified binary into a list of binaries using the specified page size.|
|[Binary.ToList](binary-tolist.md)|Converts a binary value into a list of numbers|
|[Binary.ToText](binary-totext.md)|Encodes binary data into a text form.|
|[Binary.View](binary-view.md) | Creates or extends a binary with user-defined handlers for query and action operations.|
|[Binary.ViewError](binary-viewerror.md) | Creates a modified error record which won't trigger a fallback when thrown by a handler defined on a view (via [Binary.View](binary-view.md)).|
|[Binary.ViewFunction](binary-viewfunction.md) | Creates a function that can be intercepted by a handler defined on a view (via `Binary.View`).|
|[#binary](sharpbinary.md) | Creates a binary value from numbers or text.|
