---
title: "Date.IsInPreviousNYears | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 596245ee-ef7a-41d5-b886-6771125e0180
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.IsInPreviousNYears
<code>Date.IsInPreviousNYears(**dateTime** as any, **years** as number) as nullable logical</code>
## About
Indicates whether the given datetime value <code>dateTime</code> occurs during the previous number of years, as determined by the current date and time on the system. 
* <code>dateTime</code>: A <code>date</code>, <code>datetime</code>, or <code>datetimezone</code> value to be evaluated.
* <code>years</code>: The number of years.

## Example 
Determine if the year before the current system time is in the previous two years.

<code>Date.IsInPreviousNYears(Date.AddYears(DateTime.FixedLocalNow(), -1), 2)</code>

<code>true</code>

