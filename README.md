# Blockchain_python_homework

This wallet uses the command line tool hd-wallet to create our own wallet which in this case can be used if you are the owner 
or portfolio manager and are managing crypto. 

the wallet has many functions: 
derive_wallets which allows you to You should now be able to select child accounts (and thus, private keys) by calling coins[COINTYPE][INDEX]['privkey'].

priv_key_to_account  this will convert the privkey string in a child key to an account object
that bit or web3.py can use to transact.

create_tx -- this will create the raw, unsigned transaction that contains all metadata needed to transact.

send_tx -- this will call create_tx, sign the transaction, then send it to the designated network.



