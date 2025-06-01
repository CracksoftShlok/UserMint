#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# GitHub: CracksoftShlok
# LinkedIn: https://linkedin.com/in/cracksoftshlok
# Email: shlok.k3sarwani@gmail.com
# X (Twitter): @cracksoftshlok
#
# This script is made with ❤️ and care for the infosec community.

import argparse

def generate_ad_usernames(names_file, domain='RLAB', output_file='ad_usernames.txt'):
    usernames = set()

    with open(names_file, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    for line in lines:
        parts = line.lower().split()
        if len(parts) == 2:
            first, last = parts
        elif len(parts) == 1:
            first, last = parts[0], ''
        else:
            continue

        base_usernames = {first}
        if last:
            base_usernames.update({
                last,
                f"{first}.{last}",
                f"{first}{last}",
                f"{first[0]}.{last}",
                f"{first[0]}{last}",
                f"{first}{last[0]}",
            })

        for uname in base_usernames:
            usernames.add(uname)
            usernames.add(f"{domain}\\{uname}")
            usernames.add(f"{uname}@{domain.lower()}.local")

    with open(output_file, 'w') as f:
        for uname in sorted(usernames):
            f.write(uname + '\n')

    print(f"[+] Generated {len(usernames)} usernames in {output_file}")
    print("\nMade with ❤️ and care for the infosec community — CracksoftShlok")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Active Directory-style usernames.")
    parser.add_argument("names_file", help="File with full names (e.g., 'John Doe')")
    parser.add_argument("--domain", default="RLAB", help="Domain name (default: RLAB)")
    parser.add_argument("--output", default="ad_usernames.txt", help="Output file name")

    args = parser.parse_args()
    generate_ad_usernames(args.names_file, args.domain, args.output)

