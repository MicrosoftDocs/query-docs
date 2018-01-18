---
title: "List.RemoveMatchingItems | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4285af33-6f6e-451b-84e3-768b7403678a
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.RemoveMatchingItems
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Removes all occurrences of the given values in the list.  
  
```  
List.RemoveMatchingItems(list as list, values as list, optional equationCriteria as any) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|values|The list of values to remove.|  
|optional equationCriteria|An optional equation criteria value to control equality comparison. For more information about the equationCriteria, see Parameter Values.|  
  
## Example  
  
```  
List.RemoveMatchingItems ({"A", "B", "C", "B", "A"}, {"A", "C"}) equals {"B", "B"}  
```  
