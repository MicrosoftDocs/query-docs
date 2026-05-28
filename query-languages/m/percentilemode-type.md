---
description: "Learn more about: PercentileMode.Type"
title: "PercentileMode.Type"
ms.subservice: m-source
ms.topic: reference
---

# PercentileMode.Type

## About

Specifies the percentile mode type.

## Allowed values

|Name|Value|Description|
|---|---|---|
|`PercentileMode.ExcelInc`|1|When interpolating values for [`List.Percentile`](list-percentile.md), use a method compatible with Excel's `PERCENTILE.INC`.|
|`PercentileMode.ExcelExc`|2|When interpolating values for [`List.Percentile`](list-percentile.md), use a method compatible with Excel's `PERCENTILE.EXC`.|
|`PercentileMode.SqlDisc`|3|When interpolating values for [`List.Percentile`](list-percentile.md), use a method compatible with SQL Server's `PERCENTILE_DISC`.|
|`PercentileMode.SqlCont`|4|When interpolating values for [`List.Percentile`](list-percentile.md), use a method compatible with SQL Server's `PERCENTILE_CONT`.|
