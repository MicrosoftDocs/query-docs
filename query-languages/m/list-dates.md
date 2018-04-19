---
title: "List.Dates | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Dates
<code>List.Dates(**start** as date, **count** as number, **step** as duration) as list</code>

## About
Returns a list of <code>date</code> values of size <code>count</code>, starting at <code>start</code>. The given increment, <code>step</code>, is a <code>duration</code> value that is added to every value.

## Example 1
Create a list of 5 values starting from New Year's Eve (#date(2011, 12, 31)) incrementing by 1 day(#duration(1, 0, 0, 0)).

<code>List.Dates(#date(2011, 12, 31), 5, #duration(1, 0, 0, 0))</code>

<table> <tr><td>12/31/2011 12:00:00 AM</td></tr> <tr><td>1/1/2012 12:00:00 AM</td></tr> <tr><td>1/2/2012 12:00:00 AM</td></tr> <tr><td>1/3/2012 12:00:00 AM</td></tr> <tr><td>1/4/2012 12:00:00 AM</td></tr> </table>

