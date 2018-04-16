---
title: "Text.Split | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.Split

  
## About  
Returns a list containing parts of a text value that are delimited by a separator text value.  
  
```  
Text.Split(string as text, separator as text) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The string to parse.|  
|separator|A delimiter value.|  
  
## <a name="__toc360788921"></a>Remarks  
  
-   If two delimiter values are adjacent, or appear at the beginning or end of the text value, the corresponding element in the returned list is an empty text value.  
  
-   If the text value does not contain separator, the returned array consists of a single item containing the original text value.  
  
