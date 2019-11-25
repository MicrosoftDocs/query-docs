---
title: "Binary.Compress | Microsoft Docs"
ms.date: 12/12/2018
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo
---
# Binary.Compress

## Syntax

<pre>
Binary.Compress(<b>binary</b> as nullable binary, <b>compressionType</b> as number) as nullable binary
</pre>

## About

Compresses a binary value using the given compression type. The result of this call is a compressed copy of the input. Compression types include: <ul> <li><code>Compression.GZip</code></li> <li><code>Compression.Deflate</code></li> </ul>

## Example 1
Compress the binary value.

```powerquery-m
Binary.Compress(Binary.FromList(List.Repeat({10}, 1000)), Compression.Deflate)
```

`#binary({227, 226, 26, 5, 163, 96, 20, 12, 119, 0, 0})`
