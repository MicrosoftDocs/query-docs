---
description: "Learn more about: AdoDotNet.Query"
title: "AdoDotNet.Query | Microsoft Docs"
ms.date: 02/03/2021
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan
---
# AdoDotNet.Query

## Syntax

<pre>  
AdoDotNet.Query(<b>providerName</b> as text, <b>connectionString</b> as any, <b>query</b> as text, optional <b>options</b> as nullable record) as table
</pre>

## About
Returns the result of running `query` with the connection string `connectionString` using the ADO.NET provider `providerName`. `connectionString` can be text or a record of property value pairs. Property values can either be text or number. An optional record parameter, `options`, may be provided to specify additional properties. The record can contain the following fields: 

*  `CommandTimeout` : A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.
*  `SqlCompatibleWindowsAuth` : A logical (true/false) that determines whether to produce SQL Server-compatible connection string options for Windows authentication. The default value is true.
  
Returns the result of running <code>query</code> with the connection string <code>connectionString</code> using the ADO.NET provider <code>providerName</code>. <code>connectionString</code> can be text or a record of property value pairs. Property values can either be text or number. An optional record parameter, <code>options</code>, may be provided to specify additional properties. The record can contain the following fields: <ul> <li><code>CommandTimeout</code> : A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes.</li> <li><code>SqlCompatibleWindowsAuth</code> : A logical (true/false) that determines whether to produce SQL Server-compatible connection string options for Windows authentication. The default value is true.</li> </ul> 


