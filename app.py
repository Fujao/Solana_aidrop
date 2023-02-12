from solathon.core.instructions import transfer
from solathon import Client, Transaction, PublicKey, Keypair


#If you want, change devnet for mainnet
client = Client("https://api.devnet.solana.com")


def main():
    # change wallet1, wallet2, wallet3, for your list of wallets
    list = [
        "wallet1receiver",
        "wallet2receiver",
        "wallet3receiver"
    ]
    sender = Keypair.from_private_key("SENDER PRIVATE_KEY")
    for i in list:
        receiver = PublicKey(i)
        instruction = transfer(
                from_public_key=sender.public_key,
                to_public_key=receiver, 
                lamports=10000000000 #amount of sol, this current amount = 1 SOL !!!!!!!
            )

        transaction = Transaction(instructions=[instruction], signers=[sender])

        result = client.send_transaction(transaction)
        print(f"Airdrop Sucess: {result}")

main()