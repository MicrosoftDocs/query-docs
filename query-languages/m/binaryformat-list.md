---
description: "Learn more about: BinaryFormat.List"
title: "BinaryFormat.List | Microsoft Docs"
ms.date: 3/16/2022
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

Returns a binary format that reads a sequence of items and returns a `list`. The `binaryFormat` parameter specifies the binary format of each item. There are three ways to determine the number of items read:

* If the `countOrCondition` is not specified, then the binary format will read until there are no more items.
* If the `countOrCondition` is a number, then the binary format will read that many items.
* If the `countOrCondition` is a function, then that function will be invoked for each item read. The function returns true to continue, and false to stop reading items. The final item is included in the list.
* If the `countOrCondition` is a binary format, then the count of items is expected to precede the list, and the specified format is used to read the count.

## Example 1

Read bytes until the end of the data.

**Usage**

```powerquery-m
let
    binaryData = #binary({1, 2, 3}),
    listFormat = BinaryFormat.List(BinaryFormat.Byte)
in
    listFormat(binaryData)
```

**Output**

`{1, 2, 3}`

## Example 2

Read two bytes.

**Usage**

```powerquery-m
let
    binaryData = #binary({1, 2, 3}),
    listFormat = BinaryFormat.List(BinaryFormat.Byte, 2)
in
    listFormat(binaryData)
```

**Output**

`{1, 2}`

## Example 3

Read bytes until the byte value is greater than or equal to two.

**Usage**

```powerquery-m
let
    binaryData = #binary({1, 2, 3}),
    listFormat = BinaryFormat.List(BinaryFormat.Byte, (x) => x < 2)
in
    listFormat(binaryData)
```

**Output**

`{1, 2}`
