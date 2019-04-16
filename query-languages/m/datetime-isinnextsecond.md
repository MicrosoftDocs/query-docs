---
title: "DateTime.IsInNextSecond | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInNextSecond
  
## About  

Indicates whether the given datetime value <code>dateTime</code> occurs during the next second, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current second. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul>

## Syntax

<pre>
DateTime.IsInNextSecond(<b>dateTime</b> as any) as nullable logical 
</pre>

## Example 1  

Determine if the second after the current system time is in the next second.  
  
```powerquery-m 
DateTime.IsInNextSecond(DateTime.FixedLocalNow() + #duration(0,0,0,1))
```  

`true`  
