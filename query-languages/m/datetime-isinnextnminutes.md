---
title: "DateTime.IsInNextNMinutes | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInNextNMinutes

## About  

Indicates whether the given datetime value <code>dateTime</code> occurs during the next number of minutes, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current minute. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>minutes</code>: The number of minutes.</li> </ul>

## Syntax

<pre>
DateTime.IsInNextNMinutes(<b>dateTime</b> as any, <b>minutes</b> as number) as nullable logical 
</pre>
  
### Example 1

Determine if the hour after the current system time is in the next two hours.  
  
```powerquery-m
DateTime.IsInNextNMinutes(DateTime.FixedLocalNow() + #duration(0,0,2,0), 2)  
```  
  
`true` 
