---
title: "Text.FromBinary | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 110a4629-a63d-4d4c-a966-7ba7a78fb183
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.FromBinary
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Decodes data from a binary value in to a text value using an encoding.  
  
```  
Text.FromBinary(binary as nullable binary, optional encoding as nullable number) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binary|The value to decode.|  
|optional encoding|Encoding option to apply.|  
  
Text encoding  
  
TextEncoding.Utf8 = 65001;  
  
TextEncoding.Utf16 = 1200;  
  
TextEncoding.Ascii = 20127;  
  
TextEncoding.Unicode = 1200;  
  
TextEncoding.BigEndianUnicode = 1201,  
  
TextEncoding.Windows = 1252;  
  
