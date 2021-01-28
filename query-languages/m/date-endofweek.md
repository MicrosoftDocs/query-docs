---
description: "Learn more about: Date.EndOfWeek"
title: "Date.EndOfWeek | Microsoft Docs"
ms.date: 7/29/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Date.EndOfWeek

## Syntax

<pre>
Date.EndOfWeek(<b>dateTime</b> as any, optional <b>firstDayOfWeek</b> as nullable number) as any  
</pre> 
  
## About  
Returns the last day of the week in the provided `date`, `datetime`, or `datetimezone` `dateTime`. This function takes an optional `Day`, `firstDayOfWeek`, to set the first day of the week for this relative calculation. The default value is `Day.Sunday`. <ul> <li><code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value from which the last day of the week is calculated</li> <li><code>firstDayOfWeek</code>: <i>[Optional]</i> A <code>Day.Type</code> value representing the first day of the week. Possible values are <code>Day.Sunday</code>, <code>Day.Monday</code>, <code>Day.Tuesday</code>, <code>Day.Wednesday</code>, <code>Day.Thursday</code>, <code>Day.Friday</code> and <code>Day.Saturday.</code> . The default value is <code>Day.Sunday</code>.</li> </ul>

## Example 1
Get the end of the week for 5/14/2011.

```powerquery-m
Date.EndOfWeek(#date(2011, 5, 14))
```

`#date(2011, 5, 14)`

## Example 2
Get the end of the week for 5/17/2011 05:00:00 PM -7:00, with Sunday as the first day of the week.

```powerquery-m
Date.EndOfWeek(#datetimezone(2011, 5, 17, 5, 0, 0, -7, 0), Day.Sunday)
```

`#datetimezone(2011, 5, 21, 23, 59, 59.9999999, -7, 0)`

