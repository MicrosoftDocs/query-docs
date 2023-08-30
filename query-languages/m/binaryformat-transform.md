---
description: "Learn more about: BinaryFormat.Transform"
title: "BinaryFormat.Transform"
---
# BinaryFormat.Transform

## Syntax

<pre>
BinaryFormat.Transform(<b>binaryFormat</b> as function, <b>function</b> as function) as function
</pre>

## About

Returns a binary format that will transform the values read by another binary format. The `binaryFormat` parameter specifies the binary format that will be used to read the value. The `function` is invoked with the value read, and returns the transformed value.

## Example 1

Read a byte and add one to it.

**Usage**

```powerquery-m
let
    binaryData = #binary({1}),
    transformFormat = BinaryFormat.Transform(
        BinaryFormat.Byte,
        (x) => x + 1
    )
in
    transformFormat(binaryData)
```

**Output**

`2`
