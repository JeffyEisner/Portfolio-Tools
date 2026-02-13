# Options Futures and Other Derivatives

## Chapter 1: Introduction

In the last 30 years, derivatives have become icreasingly important
Futures and options are actively traded on many exchanges.

A derivative can be defined as a financial instrument whose value depends on (or derives from) the values of other, more basic, underlying variables. 
Often the underlying variables are the prices of the traded assets.

A stock options is an example of a derivative whose value is dependent oin the price of a stock, however they can be dependent on almost any variable, from the price of hogs to the amount of snow falling at a certain ski resort.

Derivative markets come under a great deal of criticism because of their role in the credit crisis that started in 2007. Derivative products were created from portfolios of risky mortgages in the US using a procedure known as securitization. Many of the products created became worthles swhen house prices declined, leading to finanicial institutions and investors losing large ammounts of money and sparking the great recession. Chapter 8 will explain securitization and how such losses occured.

### 1.1 Exchange Traded Markets

A derivatives exchage is a market where individuals trade standardized contracts that have been defined by the exchange.
The first derivative exchanges was the Chicago Board of Trade, established in 1848 to bring farmers and merchants together.

Within a few years, the first futures-type contract was developed. It was known as a to-arrive contract.
Speculators soon became interested in the contract and found trading the contract itself to be an attractive alternative to the trading of grain itself.

The Chicago Board Options Exchange started trading call options contracts on 16 stocks in 19673. Options had traded prior to 1973, but the CBOE succeeded in creating an orderly market. Put contracts started trading on the exchange in 1977

#### Electronic Markets

Traditional derivative exchanges used the open outcry system. This involves traders physically meeting on the floor of the exchange, shouting, and using hand signals to indicate the trades they would like to carry out.

This has been rapidly outphased by electronic trading.

Electroinc Trading involves manually inputting desired values for given trades via web interfaces by keyboard and mouse.

This itself is undergoing a renaissance with the development of algorithmic trading, where computer programs are used to automatically generate and execute trades.

### 1.2 Over The Counter Markets

Not all trading of derivatives is done on exchanges. OTC Markets are important alternatives to exchanges, and measured in terms of the total volume of trading, has become much larger than exchange traded markets.

These are telephone and computer linked networks of dealers. Trades are done over the phone/computer between financial institutions and their clients . 

Telephone conversations in OTC markets are usually taped. If there is a dispute about what was agreed, the tapes are replayed to resolve the issue.
These trades are typically larger then trades on the exchange traded market.

Key Advantage: Terms of a contract do not have to be specified by an exchange. Participants are free to negotiate any mutually attractive deal.
Key Disadvantage: Usually some credit risk is involved.

#### Market Size

Both OTC and Exchange Traded Market for derivatives are huge.
Though statistics are hard to come by, the Bank for International Settlements (BIS) estimates that the notional amount of outstanding OTC derivatives was $693 trillion at the end of 2011. The notional amount of outstanding exchange traded derivatives was $70 trillion at the end of 2011. Making OTC markets roughly ~10x larger then exchange traded markets, and is expected to grow at a faster rate.

### 1.3 Forward Contracts 

A new simple derivative is a forward contract. It is an agreement to buy or sell an asset at a certain future time for a certain price. It can be contrasted with a spot contract, which is an agreement to buy or sell an asset today. A forward contract is traded in the over the counter market, usually between two financial institutions, or one of their clients.

In the contract, one party assumes a long position and agrees to buy the underlying asset on a certain specified future date for a certain specified price.
The other party assumes a short position and agrees to sell the asset on the same date for the same price.

Forward contracts can be used to hedge currency risk.

#### Payoffs from Forward Contracts

Payoffs from forward contracts 

*Spot and forward quotes for the USD/GBP exchange rate, May 24, 2010 (USD/GBP)*
| Contract Type   | Bid    | Offer  |
| --------------- | ------ | ------ |
| Spot            | 1.4407 | 1.4411 |
| 1-month forward | 1.4408 | 1.4411 |
| 2-month forward | 1.4410 | 1.4413 |
| 3-month forward | 1.4416 | 1.4422 |

Consider purchasing £1,000,000  on a 6 month contract at $1,442,200.
If the spot exchange rate were to rise to 1.5 at the end of the 6 months, the contract would be worth $57,800.
($1,500,000 - $1,442,200 = $57,800)

In General, the payoff from a long forward contract on one unit of an asset is:
*S<sub>T</sub> - K* 

The Payoff from a short position in a forward contract is:
*K - S<sub>T</sub>*

Where *K* is the delivery prices and *S<sub>T</sub>* is the spot price of the asset a maturity of the contract *T*
These payoffs can be positive or negative

Because it costs nothing to enter a forward contract, the payoff from th contract is also the trader's total gain or loss from the contract.

### 1.4 Futures Contracts
Like a forward contract, a futures contract is an agreement to buy or sell an asset at a certain future time for a certain price. However, a Futures contract is normally traded on an exchange, with specified, standardized features of the contract.

A wide variety of commodities and finnacial assets are traded as futures contracts. These include agricultural products, energy products, metals, stock indices, interest rates, and foreign exchange.

### 1.5 Options
Options are traded both on exchanges and in the over the counter market.
There are 2 types of options: call options and put options.
A call option gives the holder the right to buy the underlying asset by a certain date for a certain price.
A put option gives the holder the right to sell the underlying asset by a certain date for a certain price. 
The price in the contract is known as the *exercise/strike price*
The Date in the contract is known as the expiration date, or maturity.
It should be emphasized that an option is a right, not an obligation. The holder of the option can choose to exercise the option or not. If the holder does not exercise the option, it expires worthless.

**When reading a Call/Put option, the Bid/Offer is the price of the option contract, not the price of the underlying asset. The price of the underlying asset is given in the contract as the strike price.**

Options contracts are typically executed at 100 shares of the underlying stock, so the price of the option contract is 100 times the price of the option itself. For example, if a call option on a stock has a bid price of $0.50 and an offer price of $0.60, then the bid price for the contract is $50 and the offer price for the contract is $60.

There are 4 types of participants in options markets:
- Buyers of call options
- Sellers of call options
- Buyers of put options
- Sellers of put options

Buyers are referred to as being long the option, while sellers are referred to as being short the option.

### 1.6 Types of Traders
Three broad categories of traders in derivative markets can be identified: Hedgers, Speculators, and Arbitrageurs.

- Hedgers
Hedgers use derivatives to reduce the risk they face from future movements in a market variable.

- Speculators
Use them to bet on the future direction of a market variable

- Arbitrageurs
Take offsetting positions in two or more instruments to lock in a profit.

### 1.7 Hedgers
#### Hedging Using Forward Contracts
Suppose that an Import Company in the US knows that it will have to pay £10,000,000 on a Date August 24th.
The import Company can hedge the risk of operating in a foreign currency by buying £ at an advanced rate.
In the event of devaluation of the US dollar, the import company will be protected from the increase in the cost of the £10,000,000. In the event of an appreciation of the US dollar, the import company will not benefit from the decrease in the cost of the £10,000,000, but it will not be worse off than if it had not hedged.

Or the case of an Export Company Exporting goods to the United Kingdom, knows that it will recieve £30,000,000 in 3 months. ExportCo can hedge it's foreign exchange risk by selling £30,000,000 in the 3 month forward market at an exchange rate of 1.4410.  This would have the effect of locking the trade in at $43,230,000.

#### Hedging Using Options
Options can also be used for Hedging.

Consider aninvestor who in May of a particular year owns 1,000 shares of a stock. The share price is $28/Share. The Investor, concerned about a possible share price decline in the next 2 months, wants protection. He could buy ten July put option contracts on the stock, with a strike price of $27.50. If the quoted option price is $1, then each option contract would cost 100 x $1 = $100. The total cost of the stategy would be 10 * $100 = $1,000.
The strategy costs $1,000, but gurantees that the shares can be sold for at least $27.50 per share during the life of the option. If the price falls below, the option will be exercised, so that $27,500 is the minimum realized for the holding. When the cost of the option is taken into account, the amount realized is $26,500.

#### Comparison
There is a fundamental difference between the use of forward contracts and options for hedging. Forward contracts are designed to neutralize risk by fixing the price that the hedge will pay or receive for the underlying asset. Options contracts, by contrast, provide insurance. They offer a way for investors to protect themselves against adverse price movements in the future while still allowing them to benefit from favorable price movements.

Unlike forwards, options involve the payment of an up-front fee.

### 1.8 Speculators
Wheras hedger want to avoid exposure to adverse movements in the price of an asset, speculators want to profit from such movements. Speculators are willing to take on risk in the hope of making a profit. They are the opposite of hedgers, who want to avoid risk.

#### Speculation Using Futures
Consider a US speculator who in February thinks that the British poind will strengthn relative to the USD over the next 2 months, and is prepared to back that hunch with £250,000.

The Speculator could purchase £250,000 on the spot market in the hopes the sterling can be sold later at a higher price, while keeping the sterling in an interest bearing account.

Another option is to take a long position (we'll use 4) several Futures contracts.


