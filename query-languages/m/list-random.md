---
title: "List.Random | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Random

  
## About  
Returns a list of random numbers between 0 and 1, given the number of values to generate and an optional seed value. <ul> <li>`count`: The number of random values to generate.</li> <li>`seed`: <i>[Optional]</i> A numeric value used to seed the random number generator. If omitted a unique list of random numbers is generated each time you call the function. If you specify the seed value with a number every call to the function generates the same list of random numbers.</li> </ul>  
  
## Syntax

<pre>
List.Random(count as number, optional seed as nullable number) as { Number }  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|count|How many random numbers to return.|  
|optional seed|Randomization seed value.|  
  
## Example  
  
```powerquery-m
List.Random(10) equals { 0.44298228502412434, 0.11142372065755712, 0.81061893087374925, 0.69705957299892773, 0.84984056970562816, 0.45717397865707704, 0.27344677656583805, 0.51387371612427468, 0.14493200795023331, 0.89694489161341684 }  
```  
