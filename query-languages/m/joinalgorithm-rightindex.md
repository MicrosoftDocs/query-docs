---
description: "Learn more about: JoinAlgorithm.RightIndex"
title: "JoinAlgorithm.RightIndex | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# JoinAlgorithm.RightIndex

## About

In batches, uses the keys from the right table to do predicate-based queries against the left table. This algorithm is recommended when the left table is large, supports folding of Table.SelectRows, and contains few rows which are expected to match a right row.
