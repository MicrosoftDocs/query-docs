---
title: "List.StandardDeviation | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
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
