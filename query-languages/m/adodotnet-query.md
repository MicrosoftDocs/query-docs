---
title: "AdoDotNet.Query | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# AdoDotNet.Query
<code>AdoDotNet.Query(<b>providerName</b> as text, <b>connectionString</b> as any, <b>query</b> as text, optional <b>options</b> as nullable record) as table</code>

## About
Returns the result of running <code>query</code> with the connection string <code>connectionString</code> using the ADO.NET provider <code>providerName</code>. <code>connectionString</code> can be text or a record of property value pairs. Property values can either be text or number. An optional record parameter, <code>options</code>, may be provided to specify additional properties. The record can contain the following fields: 

*  <code>CommandTimeout</code> : A duration which controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
*  <code>SqlCompatibleWindowsAuth</code> : A logical (true/false) that determines whether to produce SQL Server-compatible connection string options for Windows authentication. The default value is true.
  