---
title: "Comparer.Equals | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Comparer.Equals

  
## About  
Returns a logical value based on the equality check over the two given values.  
  
## Syntax

<pre> 
Comparer.Equals(comparer as function, x as any, y as any) as logical  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|comparer|The comparer function is used to perform the operation.|  
|x|The left value to compare.|  
|y|The right value to compare.|  
  
## Example  
  
```powerquery-m  
let  
comparer1 = Comparer.FromCulture("en-us", false),  
comparer2 = Comparer.FromCulture("en-us", true)      
in       
[         
Test1 =  Comparer.Equals(comparer1,"a","A"), equals false   
Test2 = Comparer.Equals(comparer2,"a","A") equals true       
]  
```  
