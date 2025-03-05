---
description: "Learn more about: BinaryFormat.Text"
title: "BinaryFormat.Text"
ms.subservice: m-source
---
# BinaryFormat.Text

## Syntax

<pre>
BinaryFormat.Text(<b>length</b> as any, optional <b>encoding</b> as nullable number) as function 
</pre>

## About

Returns a binary format that reads a text value. The `length` specifies the number of bytes to decode, or the binary format of the length that precedes the text. The optional `encoding` value specifies the encoding of the text. If the `encoding` is not specified, then the encoding is determined from the Unicode byte order marks. If no byte order marks are present, then `TextEncoding.Utf8` is used.

## Example 1

Decode two bytes as ASCII text.

**Usage**

```powerquery-m
let
    binaryData = #binary({65, 66, 67}),
    textFormat = BinaryFormat.Text(2, TextEncoding.Ascii)
in
    textFormat(binaryData)
```

**Output**

`"AB"`

## Example 2

Decode ASCII text where the length of the text in bytes appears before the text as a byte.

**Usage**

```powerquery-m
let
    binaryData = #binary({2, 65, 66}),
    textFormat = BinaryFormat.Text(
        BinaryFormat.Byte,
        TextEncoding.Ascii
    )
in
    textFormat(binaryData)
```

**Output**

`"AB"`
