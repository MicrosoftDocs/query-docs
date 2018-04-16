---
title: "Binary.ToText | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Binary.ToText

  
## About  
Encodes binary data into a text form.  
  
```  
Binary.ToText(binary as binary, encoding as number) as text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binary|The binary data to encode.|  
|encoding|The encoding option to apply.|  
  
**Binary encoding**  
  
-   BinaryEncoding.Base64 = 0;  
  
-   BinaryEncoding.Hex = 1;  
  
