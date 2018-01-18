---
title: "Binary.Compress | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: dcc574cb-0be9-4b99-b9db-847c15f78f3f
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Binary.Compress
Binary.Compress(binary as nullable binary, compressionType as number) as nullable binary  
  
## About  
Compresses a binary value using the given compression type. The result of this call is a compressed copy of the input. Compression types include:  
  
|Value|  
|---------|  
|Compression.GZip|  
|Compression.Deflate|  
  
### Example 1  
Compress the binary value.  
  
```  
Binary.Compress(Binary.FromList(List.Repeat({10}, 1000)), Compression.Deflate)  
```  
  
```  
Equals: #binary({227, 226, 26, 5, 163, 96, 20, 12, 119, 0, 0})  
```  
