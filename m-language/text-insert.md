---
title: "Text.Insert | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 8bd022f9-de21-4ccb-a467-be6881fb5c0b
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Text.Insert
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a text value with newValue inserted into a text value starting at a zero-based offset.  
  
```  
Text.Insert(text as nullable text, offset as number, newText as text) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to insert into.|  
|offset|The index to insert at.|  
|newText|The new text to insert.|  
  
## <a name="__toc360788855"></a>Remark  
  
-   If offset is less than zero or more than the length of a text value, an Expression.Error is thrown.  
  
## Example  
  
```  
Text.Insert("abcdef",2,"X") equals "abXcdef"  
```  
