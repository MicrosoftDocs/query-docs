---
description: "Learn more about: JoinAlgorithm.PairwiseHash"
title: "JoinAlgorithm.PairwiseHash | Microsoft Docs"
ms.date: 9/13/2021
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# JoinAlgorithm.PairwiseHash

## About

Buffers the rows of both the left and right tables until one of the tables is completely buffered, and then performs a LeftHash or RightHash, depending on which table was buffered completely. This algorithm is recommended only for small tables.
