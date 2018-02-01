---
title: "JoinKind.FullOuter | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: cb5645ee-320c-4b8b-8dfe-60b780fb258a
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# JoinKind.FullOuter
## About
A possible value for the optional <code>JoinKind</code> parameter in <code>Table.Join</code>. A full outer join ensures that all rows of both tables appear in the result. Rows that did not have a match in the other table are joined with a default row containing null values for all of its columns.

