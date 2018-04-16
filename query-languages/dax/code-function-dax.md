---
title: "CODE Function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 4/13/2018
ms.reviewer: Minewiskan
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# CODE Function (DAX)
Returns a numeric code for the first character in a text string. The returned code corresponds to the character set used by your computer.  
  
|Operating environment|Character set|  
|-------------------------|-----------------|  
|Macintosh|Macintosh character set|  
|Windows|ANSI|  
  
## Syntax  
  
```  
CODE(text)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|text|The text for which you want the code of the first character.|  
  
## Return Value  
A numeric code for the first character in a text string.  
  
## Example  
  
|Formula|Description|Result|  
|-----------|---------------|----------|  
|=CODE("A")|Displays the numeric code for A|65|  
|=CODE("!")|Displays the numeric code for !|33|  
  
