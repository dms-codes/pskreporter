# PSK Reporter Frequency Checker

This Python script allows you to check PSK (Phase Shift Keying) frequencies and their associated statistics for a specific grid location. It uses the PSK Reporter website's API to retrieve frequency data and displays it in a tabular format.

## Usage

1. Replace the `grid` variable with the desired grid location you want to check. For example, `grid = "OI33"`.

2. Run the script. It will make an HTTP request to the PSK Reporter website's API for the specified grid location.

3. The script will display the following information for each frequency:

   - **Frequency:** The PSK frequency in Hz.
   - **Score:** A score associated with the frequency.
   - **Spots:** The number of spots or reports for the frequency.
   - **Tx:** The number of transmissions (Tx) on the frequency.
   - **Rx:** The number of receptions (Rx) on the frequency.

## Example Output

```
Frequency   Score   Spots   Tx   Rx

14,080,000  890     89      2    0

24,920,000  332     40      0    1

14,070,000  311     32      0    0

21,080,000  250     31      2    2

7,080,000   137     18      1    1

21,070,000  34      6       1    3

7,070,000   14      4       0    0

18,100,000  10      7       0    1

28,080,000  10      1       1    0
```

## Dependencies

This script relies on the `requests` library to make HTTP requests to the PSK Reporter website. Make sure you have it installed before running the script.

```bash
pip install requests
```

## Disclaimer

Please be aware of the terms and conditions of the PSK Reporter website's API and comply with any usage restrictions or limitations imposed by the service provider.
