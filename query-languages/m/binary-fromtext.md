---
title: "Binary.FromText | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Binary.FromText

  
## About  
Decodes data from a text form into binary.  
  
## Syntax

<pre>   
Binary.FromText (text as text, encoding as number) as Binary  
</pre>  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to decode.|  
|encoding|The encoding option to apply.|  
  
**Binary encoding**  
  
-   BinaryEncoding.Base64 = 0;  
  
-   BinaryEncoding.Hex = 1;  
  
