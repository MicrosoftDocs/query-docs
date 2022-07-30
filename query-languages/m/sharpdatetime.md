---
description: "Learn more about: #datetime"
title: "#datetime"
ms.date: 11/17/2021
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# #datetime

## Syntax

<pre>
#datetime(<b>year</b> as number, <b>month</b> as number, <b>day</b> as number, <b>hour</b> as number, <b>minute</b> as number, <b>second</b> as number) as datetime
</pre>

## About

Creates a datetime value from numbers representing the year, month, day, hour, minute, and (fractional) second. Raises an error if these conditions are not true:

* 1 ≤ year ≤ 9999
* 1 ≤ month ≤ 12
* 1 ≤ day ≤ 31
* 0 ≤ hour ≤ 23
* 0 ≤ minute ≤ 59
* 0 ≤ second < 60
