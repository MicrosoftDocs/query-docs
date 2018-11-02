---
title: "DateTime.IsInNextSecond | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInNextSecond

## Syntax

<pre>
DateTime.IsInNextSecond(dateTime as any) as nullable logical  
</pre>
  
## About  
Indicates whether the given datetime value occurs during the next second, as determined by the current date and time on the system.  
  
|Value|  
|---------|  
|dateTime: A datetime, or datetimezone value to be evaluated.|  
  
### Example 1  
Determine if the second after the current system time is in the next second.  
  
```powerquery-m 
DateTime.IsInNextSecond(DateTime.FixedLocalNow() + #duration(0,0,0,1))  
```  

```powerquery-m
Equals: true  
```  
