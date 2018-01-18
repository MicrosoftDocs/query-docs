---
title: "Text.ToBinary | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2ed18bb0-4438-40a2-9b34-40eb4e11dd71
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.ToBinary
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Encodes a text value into binary value using an encoding.  
  
```  
Text.ToBinary(text as nullable text,  optional encoding as nullable number,  optional includeByteOrderMark as nullable logical) as nullable binary  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|Value to encode.|  
|optional encoding|Encoding option to apply.|  
|optional includeByteOrderMark|Specify handling of byte order marks|  
  
