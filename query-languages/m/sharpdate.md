---
description: "Learn more about: #date"
title: "#date | Microsoft Docs"
ms.date: 6/21/2021
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# #date

## Syntax

<pre>
#date(<b>year</b> as number, <b>month</b> as number, <b>day</b> as number) as date
</pre>

## About

Creates a date value from whole numbers representing the year, month, and day. Raises an error if these conditions are not true:

* 1 ≤ year ≤ 9999
* 1 ≤ month ≤ 12
* 1 ≤ day ≤ 31
