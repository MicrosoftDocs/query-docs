---
title: "List.PositionOf | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 18fc0aa8-e2ac-4913-b35b-ac8fec82da4a
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.PositionOf
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Finds the first occurrence of a value in a list and returns its position.  
  
```  
List.PositionOf(list as list, value as any, optional occurrence as nullable number,optional equationCriteria as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|value|The value to check for.|  
|optional occurrence|An enum that controls the scope of operation.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values.|  
  
## Occurrence settings  
  
|**Setting**|**Description**|  
|---------------|-------------------|  
|Occurrence.First and Occurrence.Last|Returns a single position.|  
|Occurrence.All|Returns a list of positions with all occurrences.|  
  
## <a name="__toc360789324"></a>Remarks  
  
-   If the value is not found in the list, -1 is returned  
  
## Examples  
  
```  
List.PositionOf({"A", "B", "C", "D"}, "C") equals 2  
```  
  
```  
List.PositionOf({"A", "B", "C", "B", "A"}, "A", Occurrence.First)  equals 0  
```  
  
```  
List.PositionOf({"A", "B", "C", "B", "A"}, "A", Occurrence.Last) equals 4  
```  
  
```  
List.PositionOf({"A", "B", "C", "B", "A"}, "A", Occurrence.All) equals {0, 4}  
```  
