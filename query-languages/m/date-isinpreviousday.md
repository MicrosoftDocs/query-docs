---
title: "Date.IsInPreviousDay | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 40501398-7033-4c46-8546-bd4642650a70
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.IsInPreviousDay
<code>Date.IsInPreviousDay(**dateTime** as any) as nullable logical</code>
## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the previous day, as determined by the current date and time on the system. 
* <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.

## Example 
Determine if the day before the current system time is in the previous day.

<code>Date.IsInPreviousDay(Date.AddDays(DateTime.FixedLocalNow(), -1))</code>

<code>true</code>

