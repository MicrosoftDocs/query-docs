---
description: "Learn more about: Binary.ApproximateLength"
title: "Binary.ApproximateLength"
ms.topic: reference
ms.subservice: m-source
---
# Binary.ApproximateLength

## Syntax

<pre>
Binary.ApproximateLength(<b>binary</b> as nullable binary) as nullable number
</pre>

## About

Returns the approximate length of `binary`, or an error if the data source doesn't support an approximate length.

## Example 1

Get the approximate length of the binary value.

**Usage**

```powerquery-m
Binary.ApproximateLength(Binary.FromText("i45WMlSKjQUA", BinaryEncoding.Base64))
```

**Output**

`9`
