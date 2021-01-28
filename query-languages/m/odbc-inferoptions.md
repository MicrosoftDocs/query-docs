---
description: "Learn more about: Odbc.InferOptions"
title: "Odbc.InferOptions | Microsoft Docs"
ms.date: 5/22/2018
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Odbc.InferOptions

## Syntax

<pre>
Odbc.InferOptions(<b>connectionString</b> as any) as record
</pre>

## About
Returns the result of trying to infer SQL capbabilities with the connection string `connectionString` using ODBC. `connectionString` can be text or a record of property value pairs. Property values can either be text or number.
