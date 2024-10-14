# HTTP Status Checker Tool

This repository contains two Python scripts, `check_http.py` and `fast_check_http.py`, that check the HTTP status of subdomains listed in a text file. These tools are useful for web developers, system administrators, and security professionals to quickly verify the availability of web resources.

## Features

- Check the HTTP status of multiple subdomains.
- Fast checking mode with concurrent requests.
- Clear and color-coded terminal output for easy readability.
- Handles unverified HTTPS requests gracefully.

## Download

```bash
git clone https://github.com/itzNamanDev/HTTPStatus.git
```

## Enter Directory

```bash
cd HTTPStatus/
```

## Requirements

Make sure you have Python 3 installed on your machine. You can install the required dependencies using pip. See the `requirements.txt` file for the list of dependencies.

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage
**Check HTTP Status
To check the HTTP status of subdomains, run the following command:

```bash
python3 check_http.py -l <subdomains_file>
```

`subdomains_file`: A text file containing a list of subdomains (one per line) you want to check.
## Fast Check HTTP Status
For a faster check, use the fast_check_http.py script:

```bash
python3 fast_check_http.py -l <subdomains_file>
```
## Example
Given a file named subdomains.txt with the following content:

```bash
nepal.gov.np
mail.nepal.gov.np
www.nepal.gov.np
mx1.nepal.gov.np
```

You can run the following command:

```bash
python3 check_http.py -l subdomains.txt
```
or for the fast version:

```bash
python3 fast_check_http.py -l subdomains.txt
```
## Sample Output
The output will be color-coded for clarity:
```bash
[200] - mail.nepal.gov.np
[200] - www.nepal.gov.np
[TIMEOUT] - mx1.nepal.gov.np
```
`[200]` indicates a successful HTTP response.
`[TIMEOUT]` indicates that the request to the subdomain timed out.

## Notes
- You may receive warnings about unverified HTTPS requests. It is recommended to add certificate verification for production use.
- Ensure that the subdomain file is properly formatted with one subdomain per line.

## Contact Me:
- Email:
- Discord:
- Telegram:
- Twitter:
