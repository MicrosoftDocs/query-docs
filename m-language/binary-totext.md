---
title: "Binary.ToText | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 96fe975c-982e-41c9-9e6c-35b386ff344f
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Binary.ToText
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
  
