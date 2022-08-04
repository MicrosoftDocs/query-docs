---
description: "Learn more about: Binary.Decompress"
title: "Binary.Decompress"
ms.date: 3/11/2022
---
# Binary.Decompress

## Syntax

<pre> 
Binary.Decompress(<b>binary</b> as nullable binary, <b>compressionType</b> as number) as nullable binary
</pre>

## About

Decompresses a binary value using the given compression type. The result of this call is a decompressed copy of the input. Compression types include:

* [Compression.GZip](/powerquery-m/compression-gzip)
* [Compression.Deflate](/powerquery-m/compression-deflate)

## Example 1

Decompress the binary value.

**Usage**

```powerquery-m
Binary.Decompress(#binary({115, 103, 200, 7, 194, 20, 134, 36, 134, 74, 134, 84, 6, 0}), Compression.Deflate)
```

**Output**

`#binary({71, 0, 111, 0, 111, 0, 100, 0, 98, 0, 121, 0, 101, 0})`
  