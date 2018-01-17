---
title: "List.StandardDeviation | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2108d426-d8c1-4c4c-8a50-7e07952aa1c5
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.StandardDeviation
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns the standard deviation from a list of values.  List.StandardDeviation performs a sample based estimate. The result is a number for numbers, and a duration for DateTimes and Durations.  
  
```  
List.StandardDeviation(list as list) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check. If List is a list of numbers, a number is returned. An exception is thrown on an empty list or a list of items that is not type number.|  
  
## <a name="__toc360789376"></a>Remarks  
  
-   If the list is empty, an Expression.Error is thrown.  
  
## Example  
  
```  
List.StandardDeviation({1..5}) equals 1.5811388300841898  
```  
