---
description: "Learn more about: #datetime"
title: "#datetime | Microsoft Docs"
ms.date: 6/21/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# #datetime

## Syntax

<pre>
#datetime(<b>year</b> as number, <b>month</b> as number, <b>day</b> as number, <b>hour</b> as number, <b>minute</b> as number, <b>second</b> as number) as any
</pre>

## About

Creates a datetime value from numbers representing the year, month, day, hour, minute, and (fractional) second. Raises an error if these conditions are not true:

* 1 ≤ year ≤ 9999
* 1 ≤ month ≤ 12
* 1 ≤ day ≤ 31
* 0 ≤ hour ≤ 23
* 0 ≤ minute ≤ 59
* 0 ≤ second < 60
