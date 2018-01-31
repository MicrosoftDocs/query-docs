---
title: "Date.IsInPreviousNMonths | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: d7977832-d466-449e-833a-91f64855f5a8
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.IsInPreviousNMonths
<code>Date.IsInPreviousNMonths(**dateTime** as any, **months** as number) as nullable logical</code>

## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the previous number of months, as determined by the current date and time on the system. 
* <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.
* <code>months</code>: The number of months.

## Example 1
Determine if the month before the current system time is in the previous two months.

<code>Date.IsInPreviousNMonths(Date.AddMonths(DateTime.FixedLocalNow(), -1), 2)</code>

<code>true</code>

