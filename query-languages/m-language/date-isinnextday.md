---
title: "Date.IsInNextDay | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 7c44aa56-66c0-4069-856f-36a4b012db46
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.IsInNextDay
<code>Date.IsInNextDay(**dateTime** as any) as nullable logical</code>

## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the next day, as determined by the current date and time on the system. 
- <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.

## Example 
Determine if the day after the current system time is in the next day.

<code>Date.IsInNextDay(Date.AddDays(DateTime.FixedLocalNow(), 1))</code>

<code>true</code>

