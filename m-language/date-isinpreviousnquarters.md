---
title: "Date.IsInPreviousNQuarters | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 2d89707a-7035-4130-8059-513ebef41467
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.IsInPreviousNQuarters
<code>Date.IsInPreviousNQuarters(**dateTime** as any, **quarters** as number) as nullable logical</code>
## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the previous number of quarters, as determined by the current date and time on the system. 
* <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated. 
* <code>quarters</code>: The number of quarters.

## Example 1
Determine if the quarter before the current system time is in the previous two quarters.

<code>Date.IsInPreviousNQuarters(Date.AddQuarters(DateTime.FixedLocalNow(), -1), 2)</code>

<code>true</code>

