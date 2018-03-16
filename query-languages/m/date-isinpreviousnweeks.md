---
title: "Date.IsInPreviousNWeeks | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 209cad17-ec0b-4499-af84-6c2287255bb4
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.IsInPreviousNWeeks
<code>Date.IsInPreviousNWeeks(**dateTime** as any, **weeks** as number) as nullable logical</code>

## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the previous number of weeks, as determined by the current date and time on the system. 
* <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.
* <code>weeks</code>: The number of weeks.

## Example 
Determine if the week before the current system time is in the previous two weeks.

<code>Date.IsInPreviousNWeeks(Date.AddDays(DateTime.FixedLocalNow(), -7), 2)</code>

<code>true</code>

