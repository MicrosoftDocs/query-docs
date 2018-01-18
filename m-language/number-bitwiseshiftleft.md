---
title: "Number.BitwiseShiftLeft | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 919c1f49-6aed-425f-b077-d209e375d037
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Number.BitwiseShiftLeft
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the result of a bitwise shift left operation on the operands.  
  
```  
Number.BitwiseShiftLeft(x as number, y as number) as number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|x|The number to shift.|  
|y|The number of bits to shift.|  
  
## <a name="__toc360792371"></a>Remarks  
  
-   If y &gt; 0, the high-order bits shifted off are lost, and the low-order bits are filled with zeros.  
  
-   If y &lt; 0, the low-order bits shifted off are lost, and the high-order bits are filled with zeros.  
  
