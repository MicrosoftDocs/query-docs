---
title: "DateTime.IsInNextMinute | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInNextMinute

## About  

Indicates whether the given datetime value <code>dateTime</code> occurs during the next minute, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current minute. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> </ul> 
  
## Syntax

<pre>
DateTime.IsInNextMinute(<b>dateTime</b> as any) as nullable logical
</pre>

## Example 1  
Determine if the minute after the current system time is in the next minute. 
  
```powerquery-m
DateTime.IsInNextMinute(DateTime.FixedLocalNow() + #duration(0,0,1,0)) 
```  
  
`true`  
