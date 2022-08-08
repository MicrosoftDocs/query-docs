---
description: "Learn more about: Binary.Compress"
title: "Binary.Compress"
ms.date: 3/11/2022
---
# Binary.Compress

## Syntax

<pre>
Binary.Compress(<b>binary</b> as nullable binary, <b>compressionType</b> as number) as nullable binary
</pre>

## About

Compresses a binary value using the given compression type. The result of this call is a compressed copy of the input. Compression types include:

* [Compression.GZip](/powerquery-m/compression-gzip)
* [Compression.Deflate](/powerquery-m/compression-deflate)

## Example 1

Compress the binary value.

**Usage**

```powerquery-m
Binary.Compress(Binary.FromList(List.Repeat({10}, 1000)), Compression.Deflate)
```

**Output**

`#binary({227, 226, 26, 5, 163, 96, 20, 12, 119, 0, 0})`
