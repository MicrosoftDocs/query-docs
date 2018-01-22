---
title: "Date.IsInCurrentDay | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 28409b3c-ea5f-4a60-a8a3-68e646563193
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.IsInCurrentDay
<code>Date.IsInCurrentDay(**dateTime** as any) as nullable logical</code>

## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the current day, as determined by the current date and time on the system. 
- <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.

## Example 
Determine if the current system time is in the current day.

<code>Date.IsInCurrentDay(DateTime.FixedLocalNow())</code>

<code>true</code>

