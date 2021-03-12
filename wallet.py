{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "occasional-virus",
   "metadata": {},
   "outputs": [],
   "source": [
    "import subprocess \n",
    "import json\n",
    "\n",
    "\n",
    "import os\n",
    "from web3 import Web3\n",
    "from bit import *\n",
    "from constants import *\n",
    "from eth_account import Account\n",
    "from bit.network import NetworkAPI\n",
    "from bit import wif_to_key\n",
    "\n",
    "from dotenv import load_dotenv\n",
    "w3 = Web3(Web3.HTTPProvider(\"http://127.0.0.1:8545\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ideal-family",
   "metadata": {},
   "outputs": [],
   "source": [
    "load_dotenv()\n",
    "mnemonic = os.getenv(\"mnemonic\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "rocky-clinton",
   "metadata": {},
   "outputs": [],
   "source": [
    "def derive_wallets(mnemonic, coin, numderive):\n",
    "    #shell command\n",
    "    command = f'php ./derive -g --mnemonic=\"{mnemonic}\" --cols=path,address,privkey,pubkey --coin=\"{coin}\" --numderive=\"{numderive}\" --format=json'\n",
    "    # calling the subprocess\n",
    "     p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)\n",
    "        (output, err) = p.communicate()\n",
    "        p_status = p.wait()\n",
    "        keys = json.loads(output)\n",
    "        return keys\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "gross-procurement",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Create an object called coins that derives ETH and BTCTEST wallets with this function.\n",
    "def coin():\n",
    "    coin_dict = {\n",
    "        'btc-test' : derive_wallets,\n",
    "        'eth' : derive_wallets\n",
    "    }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "motivated-resource",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Linking the transaction signing libraris\n",
    "def priv_key_to_account(coin, priv_key):\n",
    "      if coin == ETH:\n",
    "        return Account.privateKeyToAccount(priv_key)\n",
    "    if coin == BTCTEST:\n",
    "        return PrivateKeyTestnet(priv_key)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "quantitative-green",
   "metadata": {},
   "outputs": [],
   "source": [
    "#create_tx -- this will create the raw, unsigned transaction that contains all metadata needed to transact.\n",
    "#This function needs the following parameters:\n",
    "def create_tx(coin,account,recipient,amount):\n",
    "    gasEstimate = w3.eth.estimateGas({\"from\":eth_acc.address, \"to\": to, \"value\": amount})\n",
    "        \n",
    "    return{\n",
    "            \"from\": eth_acc.address,\n",
    "            \"to\" : to,\n",
    "            \"value\": amount,\n",
    "            \"gasPrice\": w3.eth.gasPrice,\n",
    "            \"gas\": gasEstimate,\n",
    "            \"nonce\": w3.eth.getTransactionCount(eth_acc.address)\n",
    "        }\n",
    "    \n",
    "    \n",
    "    \n",
    "    if coin == BTCTEST:\n",
    "        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)])  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "subject-detroit",
   "metadata": {},
   "outputs": [],
   "source": [
    "#send_tx -- this will call create_tx, sign the transaction, then send it to the designated network.\n",
    "#This function needs the following parameters:\n",
    "def send_tx(coin, account, recipient, amount):\n",
    "    #You will need to check the coin, then create a raw_tx object by calling create_tx. Then, you will need to sign\n",
    "#the raw_tx using bit or web3.py (hint: the account objects have a sign transaction function within).\n",
    "    raw_tx = create_raw_tx(account, recipient, amount)\n",
    "    \n",
    "    tx_sign = eth.acc.sign_transaction(raw_tx)\n",
    "    #For ETH, return w3.eth.sendRawTransaction(signed.rawTransaction)\n",
    "        result = w3.eth.sendRawTransaction(tx_sign.rawTransaction)\n",
    "        print(result.hex())\n",
    "        return result.hex()\n",
    "    if coin == BTCTEST:\n",
    "        #For BTCTEST, return NetworkAPI.broadcast_tx_testnet(signed)\n",
    "        tx_sign = account.sign_transaction(raw_tx)\n",
    "        return NetworkAPI.broadcast_tx_testnet(tx_sign)\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
