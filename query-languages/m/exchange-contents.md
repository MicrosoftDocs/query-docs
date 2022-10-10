---
description: "Learn more about: Exchange.Contents"
title: "Exchange.Contents"
ms.date: 10/7/2022
---
# Exchange.Contents

## Syntax

<pre>
Exchange.Contents (optional <b>mailboxAddress</b> as nullable text) as table
</pre>

## About

Returns a table of contents from the Microsoft Exchange account `mailboxAddress`. If `mailboxAddress` is not specified, the default account for the credential will be used.
