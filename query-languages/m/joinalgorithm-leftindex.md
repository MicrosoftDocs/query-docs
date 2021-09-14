---
description: "Learn more about: JoinAlgorithm.LeftIndex"
title: "JoinAlgorithm.LeftIndex | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# JoinAlgorithm.LeftIndex

## About

In batches, uses the keys from the left table to do predicate-based queries against the right table. This algorithm is recommended when the right table is large, supports folding of [Table.SelectRows](/powerquery-m/table-selectrows), and contains few rows that are expected to match a left row.
