---
title: "List.ReplaceValue | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 7687d1a5-2e87-4c06-b85b-5fae183d5e4b
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.ReplaceValue
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Searches a list of values for the value and replaces each occurrence with the replacement value.  
  
```  
List.ReplaceValue(list as list,  oldValue as any, newValue as any,  replacer as function) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|oldValue|The value to replace.|  
|newValue|The new value to replace with.|  
|replacer|A function provided as replacer determines the kind of values that are being replaced. Built-in functions be be used such as  Replacer.ReplaceText and Replacer.ReplaceValue.|  
  
## <a name="__goback"></a>Example  
  
```  
List.ReplaceValue({"a", "B", "a", "a"}, "a", "A", Replacer.ReplaceText) equals {"A", "B", "A", "A"}  
```  
