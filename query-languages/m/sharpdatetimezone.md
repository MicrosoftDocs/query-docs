---
description: "Learn more about: #datetimezone"
title: "#datetimezone"
ms.date: 11/17/2021
---
# #datetimezone

## Syntax

<pre>
#datetimezone(<b>year</b> as number, <b>month</b> as number, <b>day</b> as number, <b>hour</b> as number, <b>minute</b> as number, <b>second</b> as number, <b>offsetHours</b> as number, <b>offsetMinutes</b> as number) as datetimezone
</pre>

## About

Creates a datetimezone value from numbers representing the year, month, day, hour, minute, (fractional) second, (fractional) offset-hours, and offset-minutes. Raises an error if these conditions are not true:

* 1 ≤ year ≤ 9999
* 1 ≤ month ≤ 12
* 1 ≤ day ≤ 31
* 0 ≤ hour ≤ 23
* 0 ≤ minute ≤ 59
* 0 ≤ second < 60
* -14 ≤ offset-hours + offset-minutes / 60 ≤ 14
