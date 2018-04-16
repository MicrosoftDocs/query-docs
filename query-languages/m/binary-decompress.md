---
title: "Binary.Decompress | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Binary.Decompress
<code>Binary.Decompress(<b>binary</b> as nullable binary, <b>compressionType</b> as number) as nullable binary</code>

## About
Decompresses a binary value using the given compression type. The result of this call is a decompressed copy of the input. Compression types include: 

*  <code>Compression.GZip</code>

*  <code>Compression.Deflate</code>

## Example 1
Decompress the binary value.

<code>Binary.Decompress(#binary({115, 103, 200, 7, 194, 20, 134, 36, 134, 74, 134, 84, 6, 0}), Compression.Deflate)</code>

<code>#binary({71, 0, 111, 0, 111, 0, 100, 0, 98, 0, 121, 0, 101, 0})</code>

  
