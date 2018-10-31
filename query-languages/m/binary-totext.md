---
title: "Binary.ToText | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Binary.ToText

  
## About  
Encodes binary data into a text form.  
  
## Syntax

<pre>   
Binary.ToText(binary as binary, encoding as number) as text  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binary|The binary data to encode.|  
|encoding|The encoding option to apply.|  
  
**Binary encoding**  
  
-   BinaryEncoding.Base64 = 0;  
  
-   BinaryEncoding.Hex = 1;  
  
