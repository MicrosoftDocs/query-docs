---
description: "Learn more about: JoinAlgorithm.LeftHash"
title: "JoinAlgorithm.LeftHash | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# JoinAlgorithm.LeftHash

## About

Buffers the left rows into a lookup table and streams the right rows. For each right row, the matching left rows are found via the buffered lookup table. This algorithm is recommended when the left table is small and most of the rows from the right table are expected to match a left row.
