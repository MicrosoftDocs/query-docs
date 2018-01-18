---
title: "OleDb.Query | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
applies_to: 
  - "Power BI"
ms.assetid: 1ba715b6-9a1c-432c-9251-8a6a50d3da11
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# OleDb.Query
<code>OleDb.Query(<b>connectionString</b> as any, <b>query</b> as text, optional <b>options</b> as nullable record) as table</code>

## About
Returns the result of running <code>query</code> with the connection string <code>connectionString</code> using OLE DB. <code>connectionString</code> can be text or a record of property value pairs. Property values can either be text or number. An optional record parameter, <code>options</code>, may be provided to specify additional properties. The record can contain the following fields: 
*  <code>ConnectionTimeout</code> : A duration which controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
*  <code>CommandTimeout</code> : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
*  <code>SqlCompatibleWindowsAuth</code> : A logical (true/false) that determines whether to produce SQL Server-compatible connection string options for Windows authentication. The default value is true. 
