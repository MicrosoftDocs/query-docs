---
description: "Learn more about: BinaryFormat.List"
title: "BinaryFormat.List | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# BinaryFormat.List

## Syntax

<pre>
BinaryFormat.List(<b>binaryFormat</b> as function, optional <b>countOrCondition</b> as any) as function
</pre> 
  
## About  
Returns a binary format that reads a sequence of items and returns a `list`. The `binaryFormat` parameter specifies the binary format of each item. There are three ways to determine the number of items read: <ul><li>If the <code>countOrCondition</code> is not specified, then the binary format will read until there are no more items.</li><li>If the <code>countOrCondition</code> is a number, then the binary format will read that many items.</li><li>If the <code>countOrCondition</code> is a function, then that function will be invoked for each item read. The function returns true to continue, and false to stop reading items. The final item is included in the list.</li><li>If the countOrCondition is a binary format, then the count of items is expected to precedes the list, and the specified format is used to read the count.</li></ul>

## Example 1
Read bytes until the end of the data.

```powerquery-m
let
    binaryData = #binary({1, 2, 3}),
    listFormat = BinaryFormat.List(BinaryFormat.Byte)
in
    listFormat(binaryData)
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> </table>

## Example 2
Read two bytes.

```powerquery-m
let
    binaryData = #binary({1, 2, 3}),
    listFormat = BinaryFormat.List(BinaryFormat.Byte, 2)
in
    listFormat(binaryData)
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> </table>

## Example 3
Read bytes until the byte value is greater than or equal to two.

```powerquery-m
let
    binaryData = #binary({1, 2, 3}),
    listFormat = BinaryFormat.List(BinaryFormat.Byte, (x) => x < 2)
in
    listFormat(binaryData)
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> </table>
