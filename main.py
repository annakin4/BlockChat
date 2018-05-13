import hashlib
import json
from textwrap import dedent
from time import time
from source.blockchain import Blockchain
from uuid import uuid4
from Cryptodome.PublicKey import RSA

from flask import Flask, jsonify, request

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')
node_wallet_address = "3abe345"
# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    try:
        i = values['sender']
        i = values['recipient']
        i = values['message']
        i = values['checksum']
        i = values['sent_timestamp']
    except:
        return 'Missing Values', 400

    # Create a new Transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['message'], values['checksum'], values['sent_timestamp'])

    response = {
        'message': "Message sent",
    }
    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof...
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # We must receive a reward for finding the proof.
    # The sender is "0" to signify that this node has mined a new coin.
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        credit=1,
    )

    # Forge the new Block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/main', methods=['GET'])
def main():
    return "Main Page"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)