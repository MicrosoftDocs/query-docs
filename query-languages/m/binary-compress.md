---
title: "Binary.Compress | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Binary.Compress

## Syntax

<pre>
Binary.Compress(binary as nullable binary, compressionType as number) as nullable binary  
</pre> 
 
## About  
Compresses a binary value using the given compression type. The result of this call is a compressed copy of the input. Compression types include:  
  
|Value|  
|---------|  
|Compression.GZip|  
|Compression.Deflate|  
  
### Example 1  
Compress the binary value.  
  
```powerquery-m 
Binary.Compress(Binary.FromList(List.Repeat({10}, 1000)), Compression.Deflate)  
```  
  
```powerquery-m 
Equals: #binary({227, 226, 26, 5, 163, 96, 20, 12, 119, 0, 0})  
```  
