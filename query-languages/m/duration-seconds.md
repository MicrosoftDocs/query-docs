---
title: "Duration.Seconds | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.Seconds

  
## About  
Returns a second component of a Duration value.  
  
## Syntax

<pre>
Duration.Seconds(duration as nullable duration) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|duration|The Duration to parse.|  
  
## Examples  
  
```powerquery-m
duration1 = Duration.FromText("2.05:55:20")  
```  
  
```powerquery-m
duration2 = Duration.FromText("15:50")  
```  
  
```powerquery-m
Duration.Days(duration1) equals 2  
```  
  
```powerquery-m
Duration.Hours(duration1) equals 5  
```  
  
```powerquery-m
Duration.Minutes(duration1) equals 55  
```  
  
```powerquery-m
Duration.Seconds(duration1) equals 20  
```  
  
```powerquery-m
Duration.Seconds(duration2) equals 0  
```  
