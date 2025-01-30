---
description: "Learn more about: BinaryFormat.Record"
title: "BinaryFormat.Record"
ms.subservice: m-source
---
# BinaryFormat.Record

## Syntax

<pre>
BinaryFormat.Record(<b>record</b> as record) as function
</pre>

## About

Returns a binary format that reads a record. The `record` parameter specifies the format of the record. Each field in the record can have a different binary format. If a field contains a value that is not a binary format value, then no data is read for that field, and the field value is echoed to the result.

## Example 1

Read a record containing one 16-bit integer and one 32-bit integer.

**Usage**

```powerquery-m
let
    binaryData = #binary({
        0x00, 0x01,
        0x00, 0x00, 0x00, 0x02
    }),
    recordFormat = BinaryFormat.Record([
        A = BinaryFormat.UnsignedInteger16,
        B = BinaryFormat.UnsignedInteger32
    ])
in
    recordFormat(binaryData)
```

**Output**

`[A = 1, B = 2]`
