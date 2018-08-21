---
title: "List.DateTimes | Microsoft Docs"
ms.date: 8/21/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.DateTimes
<code>List.DateTimes(<b>start</b> as datetime, <b>count</b> as number, <b>step</b> as duration) as list</code>

## About
Returns a list of <code>datetime</code> values of size <code>count</code>, starting at <code>start</code>. The given increment, <code>step</code>, is a <code>duration</code> value that is added to every value.

  
## Example  
Create a list of 10 values starting from 5 minutes before New Year's Day (#datetime(2011, 12, 31, 23, 55, 0)) incrementing by 1 minute (#duration(0, 0, 1, 0)).

<code>List.DateTimes(#datetime(2011, 12, 31, 23, 55, 0), 10, #duration(0, 0, 1, 0))</code>

<table> <tr><td>12/31/2011 11:55:00 PM</td></tr> <tr><td>12/31/2011 11:56:00 PM</td></tr> <tr><td>12/31/2011 11:57:00 PM</td></tr> <tr><td>12/31/2011 11:58:00 PM</td></tr> <tr><td>12/31/2011 11:59:00 PM</td></tr> <tr><td>1/1/2012 12:00:00 AM</td></tr> <tr><td>1/1/2012 12:01:00 AM</td></tr> <tr><td>1/1/2012 12:02:00 AM</td></tr> <tr><td>1/1/2012 12:03:00 AM</td></tr> <tr><td>1/1/2012 12:04:00 AM</td></tr> </table>
