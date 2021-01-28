---
description: "Learn more about: BinaryFormat.Length"
title: "BinaryFormat.Length | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# BinaryFormat.Length

## Syntax

<pre>
BinaryFormat.Length(<b>binaryFormat</b> as function, <b>length</b> as any) as function
</pre> 
  
## About  
Returns a binary format that limits the amount of data that can be read. Both `BinaryFormat.List` and `BinaryFormat.Binary` can be used to read until end of the data. `BinaryFormat.Length` can be used to limit the number of bytes that are read. The `binaryFormat` parameter specifies the binary format to limit. The `length` parameter specifies the number of bytes to read. The `length` parameter may either be a number value, or a binary format value that specifies the format of the length value that appears that precedes the value being read.

## Example 1
Limit the number of bytes read to 2 when reading a list of bytes.

```powerquery-m
let
    binaryData = #binary({1, 2, 3}),
    listFormat = BinaryFormat.Length(
        BinaryFormat.List(BinaryFormat.Byte),
        2
    )
in
    listFormat(binaryData)
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> </table>

## Example 2
Limit the number of byte read when reading a list of bytes to the byte value preceding the list.

```powerquery-m
let
    binaryData = #binary({1, 2, 3}),
    listFormat = BinaryFormat.Length(
        BinaryFormat.List(BinaryFormat.Byte),
        BinaryFormat.Byte
    )
in
    listFormat(binaryData)
```

<table> <tr><td>2</td></tr> </table>
