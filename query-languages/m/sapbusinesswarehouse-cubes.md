---
title: "SapBusinessWarehouse.Cubes | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# SapBusinessWarehouse.Cubes
<code>SapBusinessWarehouse.Cubes(**server** as text, **systemNumberOrSystemId** as text, **sclientId**s as text, optional **soptionsOrLogonGroup**s as any, optional **soptions**s as nullable record) as table</code>

## About
Returns a table of InfoCubes and queries grouped by InfoArea from an SAP Business Warehouse instance at server <code>server</code> with system number <code>systemNumberOrSystemId</code> and Client ID <code>clientId</code>. An optional record parameter, <code>optionsOrLogonGroup</code>, may be specified to control options. 