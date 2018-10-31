---
title: "List.Numbers | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Numbers

  
## About  
Returns a list of numbers from size count starting at initial, and adds an increment.  The increment defaults to 1.  
  
## Syntax

<pre>
List.Numbers(start as number, count as number, optional increment as nullable number) as { Number }  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|start|The first number in the sequence.|  
|count|How many numbers to return.|  
|optional increment|The number to increment each number.|  
  
## Examples  
  
```powerquery-m
List.Numbers(1, 5) equals {1, 2, 3, 4, 5}  
```  
  
```powerquery-m
List.Numbers(1, 8, 3) equals {1, 4, 7, 10, 13, 16, 19, 22}  
```  
