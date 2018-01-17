---
title: "Text.At | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c6dfb8bc-6ba6-46fd-9c9a-6ca9964bb404
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.At
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a character starting at a zero-based offset.  
  
```  
Text.At(value as nullable text, index as number) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to parse.|  
|index|The index of the character to return.|  
  
## <a name="__toc360788840"></a>Remarks  
  
-   If the offset is greater than index, an Expression.Error is thrown.  
  
## Examples  
  
```  
Text.At("abcd", 0) equals "a"  
```  
  
```  
Text.At("abcd", 5) equals error  
```  
