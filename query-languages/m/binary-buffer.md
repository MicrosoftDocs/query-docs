---
title: "Binary.Buffer | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan
---
# Binary.Buffer

## Syntax

<pre>
Binary.Buffer(<b>binary</b> as nullable binary) as nullable binary
</pre>

## About
Buffers the binary value in memory. The result of this call is a stable binary value, which means it will have a deterministic length and order of bytes.

## Example 1

Create a stable version of the binary value.

```powerquery-m
Binary.Buffer(Binary.FromList({0..10}))
```

`#binary({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10})`

