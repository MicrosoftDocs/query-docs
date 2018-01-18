---
title: "List.PositionOfAny | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: e2273ae9-05d4-44f9-a862-c7457ecd8a3a
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.PositionOfAny
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Finds the first occurrence of any value in values and returns its position.  
  
```  
List.PositionOfAny(list as list, values as list, optional occurrence as nullable number, optional equationCriteria as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|values|The list of values to check for.|  
|optional occurrence|An enum that controls the scope of operation.|  
|optional equationCriteria|An optional equation criteria value to control equality comparisons. For more information about equality comparisons, see Parameter Values .|  
  
## Occurrence settings  
  
|**Setting**|**Description**|  
|---------------|-------------------|  
|Occurrence.First and Occurrence.Last|Returns a single position.|  
|Occurrence.All|Returns a list of positions with all occurrences.|  
  
## <a name="__toc360789328"></a>Remarks  
  
-   If the value is not found in the list, -1 is returned  
  
## Examples  
  
```  
List.PositionOfAny({"A", "B", "C", "D"}, {"B", "C"}) equals 1  
```  
`List.PositionOfAny({"A", "B", "C", "B", "A"}, {"A", "B"}, Occurrence.First) equals 0`  
  
```  
List.PositionOfAny({"A", "B", "C", "B", "A"}, {"A", "B"}, Occurrence.Last) equals 4  
```  
  
```  
List.PositionOfAny({"A", "B", "C", "B", "A"}, {"A", "B"}, Occurrence.All) equals {0, 1, 3, 4}  
```  
