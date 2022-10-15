# Majority Judgment Data testing

[![MIT](https://img.shields.io/github/license/MieuxVoter/majority-judgment-library-python?style=for-the-badge)](./LICENSE)
[![Join the Discord chat at https://discord.gg/rAAQG9S](https://img.shields.io/discord/705322981102190593.svg?style=for-the-badge)](https://discord.gg/rAAQG9S)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FMieuxVoter%2Fmajority-judgment-fixtures-generator-python%2Fbadge%3Fref%3Dmain&style=for-the-badge)](https://actions-badge.atrox.dev/MieuxVoter/majority-judgment-fixtures-generator-python/goto?ref=main)

This is generating a set of `*.yml` files for testing librairies.
The set of files can be find on the Releases.


## Specification format (example)

To compare your implementation, you need to produce files in the same format. See for example that one:

```yaml
algorithm: 
  name: majority_judgment
  options: {}
ballots:
- [0, 3, 2]
- [2, 5, 2]
- [1, 1, 5]
- [5, 3, 5]
ranking: {1: 2, 2: 0, 3: 1}
```


## Local development

Create a virtual environment and install dependencies:

```bash
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

Now, you can generate files

```bash
python generate_test.py --output /path/to/tests/
```

