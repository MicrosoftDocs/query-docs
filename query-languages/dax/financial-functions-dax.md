---
title: "Financial functions (DAX) | Microsoft Docs"
ms.service: powerbi 
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend

---
# Financial functions

Financial functions in DAX are used in formulas that perform financial calculations, such as net present value and rate of return. These functions are similar to financial functions used in Microsoft Excel.
  
## In this category

|Function  |Description  |
|---------|---------|
|[ACCRINT](accrint-function-dax.md)     |  Returns the accrued interest for a security that pays periodic interest.      |
|[ACCRINTM](accrintm-function-dax.md)     |   Returns the accrued interest for a security that pays interest at maturity.     |
|[AMORDEGRC](amordegrc-function-dax.md)     |   Returns the depreciation for each accounting period.     |
|[AMORLINC](amorlinc-function-dax.md)     |   Returns the depreciation for each accounting period.      |
|[COUPDAYBS](coupdaybs-function-dax.md)     |    Returns the number of days from the beginning of a coupon period until its settlement date.    |
|[COUPDAYS](coupdays-function-dax.md)     |    Returns the number of days in the coupon period that contains the settlement date.    |
|[COUPDAYSNC](coupdaysnc-function-dax.md)     |    Returns the number of days from the settlement date to the next coupon date.   |
|[COUPNCD](coupncd-function-dax.md)     |   Returns the next coupon date after the settlement date.     |
|[COUPNUM](coupnum-function-dax.md)     |   Returns the number of coupons payable between the settlement date and maturity date, rounded up to the nearest whole coupon.     |
|[COUPPCD](couppcd-function-dax.md)     |   Returns the previous coupon date before the settlement date.     |
|[CUMIPMT](cumipmt-function-dax.md)     |   Returns the cumulative interest paid on a loan between start_period and end_period.     |
|[CUMPRINC](cumprinc-function-dax.md)     |    Returns the cumulative principal paid on a loan between start_period and end_period.    |
|[DB](db-function-dax.md)     |   Returns the depreciation of an asset for a specified period using the fixed-declining balance method.     |
|[DDB](ddb-function-dax.md)     |    Returns the depreciation of an asset for a specified period using the double-declining balance method or some other method you specify.    |
|[DISC](disc-function-dax.md)     |    Returns the discount rate for a security.        |
|[DOLLARDE](dollarde-function-dax.md)     |    Converts a dollar price expressed as an integer part and a fraction part, such as 1.02, into a dollar price expressed as a decimal number.      |
|[DOLLARFR](dollarfr-function-dax.md)     |    Converts a dollar price expressed as an integer part and a fraction part, such as 1.02, into a dollar price expressed as a decimal number.     |
|[DURATION](duration-function-dax.md)     |    Returns the Macauley duration for an assumed par value of $100.    |
|[EFFECT](effect-function-dax.md)     |   Returns the effective annual interest rate, given the nominal annual interest rate and the number of compounding periods per year.     |
|[FV](fv-function-dax.md)     |   Calculates the future value of an investment based on a constant interest rate.     |
|[INTRATE](intrate-function-dax.md)     |   Returns the interest rate for a fully invested security.     |
|[IPMT](ipmt-function-dax.md)     |    Returns the interest payment for a given period for an investment based on periodic, constant payments and a constant interest rate.    |
|[ISPMT](ispmt-function-dax.md)     |    Calculates the interest paid (or received) for the specified period of a loan (or investment) with even principal payments.    |
|[MDURATION](mduration-function-dax.md)     |    Returns the modified Macauley duration for a security with an assumed par value of $100.    |
|[NOMINAL](nominal-function-dax.md)     |   Returns the nominal annual interest rate, given the effective rate and the number of compounding periods per year.     |
|[NPER](nper-function-dax.md)     |    Returns the number of periods for an investment based on periodic, constant payments and a constant interest rate.    |
|[ODDFPRICE](oddfprice-function-dax.md)     |    Returns the price per \$100 face value of a security having an odd (short or long) first period.    |
|[ODDFYIELD](oddfyield-function-dax.md)     |    Returns the yield of a security that has an odd (short or long) first period.     |
|[ODDLPRICE](oddlprice-function-dax.md)     |    Returns the price per $100 face value of a security having an odd (short or long) last coupon period.    |
|[ODDLYIELD](oddlyield-function-dax.md)     |    Returns the yield of a security that has an odd (short or long) last period.    |
|[PDURATION](pduration-function-dax.md)     |    Returns the number of periods required by an investment to reach a specified value.    |
|[PMT](pmt-function-dax.md)     |   Calculates the payment for a loan based on constant payments and a constant interest rate.     |
|[PPMT](ppmt-function-dax.md)     |    Returns the payment on the principal for a given period for an investment based on periodic, constant payments and a constant interest rate.   |
|[PRICE](price-function-dax.md)     |     Returns the price per \$100 face value of a security that pays periodic interest.   |
|[PRICEDISC](pricedisc-function-dax.md)     |   Returns the price per \$100 face value of a discounted security.     |
|[PRICEMAT](pricemat-function-dax.md)     |    Returns the price per $100 face value of a security that pays interest at maturity.    |
|[PV](pv-function-dax.md)     |   Calculates the present value of a loan or an investment, based on a constant interest rate.      |
|[RATE](rate-function-dax.md)     |  Returns the interest rate per period of an annuity.       |
|[RECEIVED](received-function-dax.md)     |    Returns the amount received at maturity for a fully invested security.    |
|[RRI](rri-function-dax.md)     |    Returns an equivalent interest rate for the growth of an investment.    |
|[SLN](sln-function-dax.md)     |    Returns the straight-line depreciation of an asset for one period.   |
|[SYD](syd-function-dax.md)     |    Returns the sum-of-years' digits depreciation of an asset for a specified period.    |
|[TBILLEQ](tbilleq-function-dax.md)     |    Returns the bond-equivalent yield for a Treasury bill.    |
|[TBILLPRICE](tbillprice-function-dax.md)     |    Returns the price per $100 face value for a Treasury bill.    |
|[TBILLYIELD](tbillyield-function-dax.md)     |    Returns the yield for a Treasury bill.    |
|[VDB](vdb-function-dax.md)     |    Returns the depreciation of an asset for any period you specify, including partial periods, using the double-declining balance method or some other method you specify.    |
|[XIRR](xirr-function-dax.md)     |  Returns the internal rate of return for a schedule of cash flows that is not necessarily periodic.       |
|[XNPV](xnpv-function-dax.md)      |  Returns the present value for a schedule of cash flows that is not necessarily periodic.       |
|[YIELD](yield-function-dax.md)     |   Returns the yield on a security that pays periodic interest.    |
|[YIELDDISC](yielddisc-function-dax.md)     |   Returns the annual yield for a discounted security.    |
|[YIELDMAT](yieldmat-function-dax.md)     |     Returns the annual yield of a security that pays interest at maturity.   |
