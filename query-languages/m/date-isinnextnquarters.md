---
title: "Date.IsInNextNQuarters | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.IsInNextNQuarters
<code>Date.IsInNextNQuarters(**dateTime** as any, **quarters** as number) as nullable logical</code>
## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the next number of quarters, as determined by the current date and time on the system. 
- <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated. 
- <code>quarters</code>: The number of quarters.

## Example 
Determine if the quarter after the current system time is in the next two quarters.

<code>Date.IsInNextNQuarters(Date.AddQuarters(DateTime.FixedLocalNow(), 1), 2)</code>

<code>true</code>

