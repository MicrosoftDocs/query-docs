---
title: "Date.IsInNextNWeeks | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3a6b05ed-02c7-4cf6-b61a-a09b0698c4db
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Date.IsInNextNWeeks
<code>Date.IsInNextNWeeks(**dateTime** as any, **weeks** as number) as nullable logical</code>

## About

Indicates whether the given datetime value <code>dateTime</code> occurs during the next number of weeks, as determined by the current date and time on the system. 
- <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated. 
- <code>weeks</code>: The number of weeks.

## Example 
Determine if the week after the current system time is in the next two weeks.

<code>Date.IsInNextNWeeks(Date.AddDays(DateTime.FixedLocalNow(), 7), 2)</code>

<code>true</code>

