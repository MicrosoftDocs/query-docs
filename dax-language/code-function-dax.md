---
title: "CODE Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 110f85a8-4fb3-4675-ba0e-9c8a2e0d1944
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
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
  
