# Snoopy

> Snoopy dog found something interesting.
> 
> Can you get something interesting out of the 256 bytes he found?
> 
> `IKIANJKDPKKAPJIDNKKAPNBHELCBHMGGDLOBLIPCKNAHFOEEBNFHALLBOMPGKJADFKDAGMNGIIGCDPEFBINCIPNFIMKGPPLFOMLGOKFAAIECBPJFM</Password><Domain type="NT">CORP</Domain></Credentials><ClientName>THUMPERSDESK7</ClientName><ClientType>ica30</ClientType><ClientAddress>10.1`

This was encoded as "ctx1", using the dec.py from
https://darthnull.org/good-fun-bad-crypto/ we can solve the flag:

`he2022{ctx1_41nt_3nKryp710n!}`
