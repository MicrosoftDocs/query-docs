---
description: "Learn more about: #time"
title: "#time | Microsoft Docs"
ms.date: 6/21/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# #time

## Syntax

<pre>
#time(<b>hour</b> as number, <b>minute</b> as number, <b>second</b> as number) as time
</pre>

## About

Creates a time value from numbers representing the hour, minute, and (fractional) second. Raises an error if these conditions are not true:

* 0 ≤ hour ≤ 24
* 0 ≤ minute ≤ 59
* 0 ≤ second < 60
* if hour is 24, then minute and second must be 0
