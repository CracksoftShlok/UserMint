# Active Directory Username Generation for Pentesting

<img src="https://github.com/CracksoftShlok/UserMint/blob/main/Banner.png?raw=true" alt="Alt text" style="width: 100%; height: auto;" />

In the world of cybersecurity and penetration testing, especially when it comes to Active Directory (AD), knowing usernames is half the battle. Once you have valid usernames, you can test for weak passwords, misconfigurations, or even launch attacks like AS-REP roasting or password spraying.

But there’s a big problem: **How do you quickly create a list of usernames from full names?**  
Manually crafting them? That’s slow, boring, and easy to mess up.

That’s why I built a **Python-based Active Directory Username Generator Script** — a simple tool that takes a list of full names and generates **realistic, professional AD-style usernames** used in corporate environments.

Let’s break it all down…

#### What Does This Script Do?

This script automates the process of generating **AD-style usernames** from a list of full names.

So let’s say you collected names like:
```
John Doe
Alice Johnson
Raj Kumar
```

The script will convert them into:
```
jdoe
john.doe
johnd
j.kumar
rajk
...
```

It even gives you domain formats like:
```
RLAB\jdoe
jdoe@rlab.local
```

These are the exact formats used inside real-world corporate networks. That means when you’re running pentests or red team assessments, these usernames have a much higher chance of being valid.

#### Why Username Generation Matters in Pentesting ?

Active Directory is the **heart of almost every enterprise network**. If you're doing an internal pentest, password audit, or even external recon — **you need valid usernames** before you can do anything meaningful.

Once you have usernames, you can:

- Test for weak passwords with **password spraying**
- Launch **AS-REP roasting** attacks
- Test **Kerberos login enumeration** (e.g. with `kerbrute`)
- Use usernames in **SMB, LDAP, WinRM** tools
- Run phishing simulations or create **dummy AD labs**

#### How the Script Works
The script reads a file full of names and generates usernames in different styles:

```
python3 ad_username_generator.py names.txt --domain RLAB --output usernames.txt
```

It creates usernames like:

- `jdoe`
- `john.doe`
- `john.d`
- `doej`
- `RLAB\jdoe`
- `jdoe@rlab.local`

The script handles names with one or two parts, filters out blanks, and makes sure you get a clean, sorted list in the output file.

#### Why This Script is Better Than Doing It Manually ?

This script is super fast and efficient, designed to handle large lists of names in just seconds without breaking a sweat. Its accuracy ensures that every generated username closely matches real-world formats used in enterprise Active Directory environments, minimizing false positives during enumeration. Whether you're working with a handful of names or processing hundreds, the script delivers consistently clean, reliable output. Best of all, the generated usernames are immediately compatible with popular offensive security tools like `kerbrute`, `GetNPUsers.py`, and `CrackMapExec`, making it an ideal companion for any red teamer or pentester conducting reconnaissance or credential-based attacks in AD environments.

#### Real-World Scenarios Where This Script Shines

Imagine you’re on an internal assessment. You scrape some names from email headers, LinkedIn, or old documentation. Instead of guessing usernames one-by-one, you run this script, feed the list into `kerbrute`, and bam — you’ve got a set of valid AD users within minutes.

Here’s how it might plug into your toolkit:
```
# Use it with kerbrute to find valid users
kerbrute userenum -d RLAB.local usernames.txt --dc 192.168.1.10

# Use it with Impacket for AS-REP roasting
GetNPUsers.py RLAB.local/ -usersfile usernames.txt -no-pass

# Use it with CrackMapExec to spray credentials
crackmapexec smb 192.168.1.0/24 -u usernames.txt -p 'Winter2024!'
```

#### Customize It Your Way

Want more control? You can tweak or extend the script to:

- Add middle initials (e.g. `john.r.doe`)
- Use underscores or hyphens (`john_doe`, `john-doe`)
- Handle CSV or Excel name imports
- Auto-integrate into OSINT tools or LinkedIn scrapers

#### Built by a Pentester, for Pentesters

This isn’t just another tool.

This is a **daily driver** — a script that saves time, boosts accuracy, and speeds up your workflow. Whether you’re a red teamer, blue teamer, security engineer, or student building your own lab, this tool gives you the edge when working with Active Directory.

No fluff. Just function.
And best of all, it's made with ❤️ and care for the infosec community.

I Hope, You Love it!
