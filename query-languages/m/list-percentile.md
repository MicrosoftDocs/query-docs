---
description: "Learn more about: List.Percentile"
title: "List.Percentile | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# List.Percentile

## Syntax

<pre>
List.Percentile(<b>list</b> as list, <b>percentiles</b> as any, optional <b>options</b> as nullable record) as any
</pre>
  
## About

Returns one or more sample percentiles of the list `list`. If the value `percentiles` is a number between 0.0 and 1.0, it will be treated as a percentile and the result will be a single value corresponding to that probability. If the value `percentiles` is a list of numbers with values between 0.0 and 1.0, the result will be a list of percentiles corresponding to the input probability.

The PercentileMode option in `options` can be used by advanced users to pick a more-specific interpolation method but is not recommended for most uses. Predefined symbols [PercentileMode.ExcelInc](/powerquery-m/percentilemode-excelinc) and [PercentileMode.ExcelExc](/powerquery-m/percentilemode-excelexc) match the interpolation methods used by the Excel functions `PERCENTILE.INC` and `PERCENTILE.EXC`. The default behavior matches **PercentileMode.ExcelInc**. The symbols [PercentileMode.SqlCont](/powerquery-m/percentilemode-sqlcont) and [PercentileMode.SqlDisc](/powerquery-m/percentilemode-sqldisc) match the SQL Server behavior for `PERCENTILE_CONT` and `PERCENTILE_DISC`, respectively.

## Example 1

Find the first quartile of the list `{5, 3, 1, 7, 9}`.

**Usage**

```powerquery-m
List.Percentile({5, 3, 1, 7, 9}, 0.25)
```

**Output**

`3`

## Example 2

Find the quartiles of the list `{5, 3, 1, 7, 9}` using an interpolation method matching Excel's `PERCENTILE.EXC`.

**Usage**

```powerquery-m
List.Percentile({5, 3, 1, 7, 9}, {0.25, 0.5, 0.75}, [PercentileMode=PercentileMode.ExcelExc])
```

**Output**

`{2, 5, 8}`
