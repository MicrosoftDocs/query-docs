---
description: "Learn more about: BinaryFormat.Choice"
title: "BinaryFormat.Choice"
ms.subservice: m-source
---
# BinaryFormat.Choice

## Syntax

<pre>
BinaryFormat.Choice(
    <b>binaryFormat</b> as function,
    <b>chooseFunction</b> as function,
    optional <b>type</b> as nullable type,
    optional <b>combineFunction</b> as nullable function
) as function
</pre>

## About

Returns a binary format that chooses the next binary format based on a value that has already been read. The binary format value produced by this function works in stages:

* The binary format specified by the `binaryFormat` parameter is used to read a value.
* The value is passed to the choice function specified by the `chooseFunction` parameter.
* The choice function inspects the value and returns a second binary format.
* The second binary format is used to read a second value.
* If the combine function is specified, then the first and second values are passed to the combine function, and the resulting value is returned.
* If the combine function is not specified, the second value is returned.
* The second value is returned.

The optional `type` parameter indicates the type of binary format that will be returned by the choice function. Either `type any`, `type list`, or `type binary` may be specified. If the `type` parameter is not specified, then `type any` is used. If `type list` or `type binary` is used, then the system may be able to return a streaming `binary` or `list` value instead of a buffered one, which may reduce the amount of memory necessary to read the format.

## Example 1

Read a list of bytes where the number of elements is determined by the first byte.

**Usage**

```powerquery-m
let
    binaryData = #binary({2, 3, 4, 5}),
    listFormat = BinaryFormat.Choice(
        BinaryFormat.Byte,
        (length) => BinaryFormat.List(BinaryFormat.Byte, length)
    )
in
    listFormat(binaryData)
```

**Output**

`{3,4}`

## Example 2

Read a list of bytes where the number of elements is determined by the first byte, and preserve the first byte read.

**Usage**

```powerquery-m
let
    binaryData = #binary({2, 3, 4, 5}),
    listFormat = BinaryFormat.Choice(
        BinaryFormat.Byte,
        (length) => BinaryFormat.Record([
            length = length,
            list = BinaryFormat.List(BinaryFormat.Byte, length)
        ])
    )
in
    listFormat(binaryData)
```

**Output**

`[length = 2, list = {3, 4}]`

## Example 3

Read a list of bytes where the number of elements is determined by the first byte using a streaming list.

**Usage**

```powerquery-m
let
    binaryData = #binary({2, 3, 4, 5}),
    listFormat = BinaryFormat.Choice(
        BinaryFormat.Byte,
        (length) => BinaryFormat.List(BinaryFormat.Byte, length),
        type list
    )
in
    listFormat(binaryData)
```

**Output**

`{3, 4}`
