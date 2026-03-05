---
description: "Learn more about: #binary"
title: "#binary"
ms.subservice: m-source
ms.topic: reference
---
# #binary
## Syntax

<pre>
#binary(<b>value</b> as any) as any
</pre>

## About

Creates a binary value from a list of numbers or a base 64 encoded text value.

## Example 1

Create a binary value from a list of numbers.

**Usage**

```powerquery-m
#binary({0x30, 0x31, 0x32})
```

**Output**

`Text.ToBinary("012")`

## Example 2

Create a binary value from a base 64 encoded text value.

**Usage**

```powerquery-m
#binary("1011")
```

**Output**

`Binary.FromText("1011", BinaryEncoding.Base64)`
