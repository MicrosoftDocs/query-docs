---
description: "Learn more about: Essbase.Cubes"
title: "Essbase.Cubes | Microsoft Docs"
ms.date: 02/03/2021
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Essbase.Cubes

## Syntax

<pre>
Essbase.Cubes(<b>url</b> as text, optional <b>options</b> as nullable record) as table
</pre>

## About  

Returns a table of cubes grouped by Essbase server from an Essbase instance at APS server `url`. An optional record parameter, `options`, may be specified to control the following options: 
- `CommandTimeout` : A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is ten minutes. 


