---
title: "List.StandardDeviation | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.StandardDeviation

  
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
