# Ethereum Integration Service

## Introduction

The Ethereum Integration Service is a Python-based project designed to facilitate payments using Ethereum. This service calculates the value of Ethereum in USD and BRL and enables the sending and receiving of payments by integrating with the Ethereum blockchain.

## Features

- Calculate Ethereum value in USD and BRL.
- Send and receive payments through Ethereum.
- Integration with the Ethereum blockchain for secure and reliable transactions.

## Requirements

- Python 3.12
- `web3` library
- `requests` library
- `dotenv` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/ethereum-integration-service.git
    cd ethereum-integration-service
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3.12 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**

    Create a `.env` file in the root directory and add your Ethereum node URL and other necessary configurations:

    ```env
    ETHEREUM_NODE_URL=<Your Ethereum Node URL>
    ```

## Usage

### Calculating Ethereum Value

To calculate the value of Ethereum in USD and BRL, use the `calculate_value.py` script:

```bash
python calculate_value.py
