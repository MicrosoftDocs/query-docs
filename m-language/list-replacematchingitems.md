---
title: "List.ReplaceMatchingItems | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0ab144d3-7c08-4b3a-9955-101311566763
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.ReplaceMatchingItems
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Replaces occurrences of existing values in the list with new values using the provided equationCriteria. Old and new values are provided by the replacements parameters. An optional equation criteria value can be specified to control equality comparisons. For details of replacement operations and equation criteria, see Parameter Values.  
  
```  
List.ReplaceMatchingItems(list as list, replacements as any ,optional equationCriteria as any) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|replacements|The replacements to make.|  
|optional equationCriteria|An optional equation criteria value to control equality testing.|  
  
## Examples  
  
```  
List.ReplaceMatchingItems ({1, 2, 3, 4, 5}, {{2, -2}}) equals { 1, -2, 3, 4, 5}  
```  
  
```  
List.ReplaceMatchingItems ({1, 2, 3, 4, 5}, {{2, -2}, {3, -3}}) equals { 1, -2, -3, 4, 5}  
```  
