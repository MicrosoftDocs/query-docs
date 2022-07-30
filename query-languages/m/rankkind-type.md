---
description: "Learn more about: RankKind.Type"
title: "RankKind.Type | Microsoft Docs"
ms.date: 5/19/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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
