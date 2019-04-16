---
title: "DateTime.IsInPreviousNMinutes | Microsoft Docs"
ms.date: 4/16/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.IsInPreviousNMinutes

## About  

Indicates whether the given datetime value <code>dateTime</code> occurs during the previous number of minutes, as determined by the current date and time on the system. Note that this function will return false when passed a value that occurs within the current minute. <ul> <li><code>dateTime</code>: A <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.</li> <li><code>minutes</code>: The number of minutes.</li> </ul>

## Syntax

<pre>
DateTime.IsInPreviousNMinutes(<b>dateTime</b> as any, <b>minutes</b> as number) as nullable logical 
</pre>
  
## Example 1  

Determine if the minute before the current system time is in the previous two minutes.  
  
```powerquery-m
Determine if the minute before the current system time is in the previous two minutes.  
```

`true`
