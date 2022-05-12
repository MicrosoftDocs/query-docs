---
description: "Learn more about: JoinAlgorithm.Type"
title: "JoinAlgorithm.Type | Microsoft Docs"
ms.date: 5/11/2022
ms.service: powerquery
ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# JoinAlgorithm.Type

## Definition

Specifies the join algorithm to be used in the join operation.

## Allowed values

|Allowed value|Value|Description|
| ------- | --- | ----------- |
|**Dynamic**|0| Automatically chooses a join algorithm based on inspecting the initial rows and metadata of both tables.|
|**PairwiseHash**|1| Buffers the rows of both the left and right tables until one of the tables is completely buffered, and then performs a LeftHash or RightHash, depending on which table was buffered completely. This algorithm is recommended only for small tables.|
|**SortMerge**|2| Performs a streaming merge based on the assumption that both tables are sorted by their join keys. While efficient, it will return incorrect results if the tables aren't sorted as expected.|
|**LeftHash**|3| Buffers the left rows into a lookup table and streams the right rows. For each right row, the matching left rows are found via the buffered lookup table. This algorithm is recommended when the left table is small and most of the rows from the right table are expected to match a left row.|
|**RightHash**|4| Buffers the right rows into a lookup table and streams the left rows. For each left row, the matching right rows are found via the buffered lookup table. This algorithm is recommended when the right table is small and most of the rows from the left table are expected to match a right row.|
|**LeftIndex**|5| In batches, uses the keys from the left table to do predicate-based queries against the right table. This algorithm is recommended when the right table is large, supports folding of Table.SelectRows, and contains few rows that are expected to match a left row.|
|**RightIndex**|6| In batches, uses the keys from the right table to do predicate-based queries against the left table. This algorithm is recommended when the left table is large, supports folding of Table.SelectRows, and contains few rows that are expected to match a right row.|

## Applies to

* [Table functions](table-functions.md)
