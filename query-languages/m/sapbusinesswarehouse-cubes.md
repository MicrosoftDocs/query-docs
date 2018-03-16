---
title: "SapBusinessWarehouse.Cubes | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 51c42e8d-2df2-4110-9b98-a97d1a27df8e
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# SapBusinessWarehouse.Cubes
<code>SapBusinessWarehouse.Cubes(**server** as text, **systemNumberOrSystemId** as text, **sclientId**s as text, optional **soptionsOrLogonGroup**s as any, optional **soptions**s as nullable record) as table</code>

## About
Returns a table of InfoCubes and queries grouped by InfoArea from an SAP Business Warehouse instance at server <code>server</code> with system number <code>systemNumberOrSystemId</code> and Client ID <code>clientId</code>. An optional record parameter, <code>optionsOrLogonGroup</code>, may be specified to control options. 