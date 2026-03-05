---
description: "Learn more about: RankKind.Type"
title: "RankKind.Type"
ms.subservice: m-source
ms.topic: reference
---
# RankKind.Type

## Definition

Specifies the precise ranking method.

## Allowed values

|Name|Value|Description|
| ------- | -- | --------- |
|**RankKind.Competition**|0|Items which compare as equal receive the same ranking number and then a gap is left before the next ranking.|
|**RankKind.Dense**|1|Items which compare as equal receive the same ranking number and the next item is numbered consecutively with no gap.|
|**RankKind.Ordinal**|2|All items are given a unique ranking number even if they compare as equal.|

## Applies to

* [Table functions](table-functions.md)
